import os
import json
from groq import Groq

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def classify_message(message: str) -> dict:
    """
    Classify a single support message using OpenAI API.
    Returns a dict with category and priority.
    """
    prompt = f"""You are a support ticket classifier.
Classify the given message into:
- Category: Billing, Technical Issue, Account, General Inquiry
- Priority: High (urgent or blocking issues), Medium (moderate issues), Low (general or informational queries)

Return ONLY JSON in this exact format, no extra text:
{{
  "category": "",
  "priority": ""
}}

Message: "{message}"
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    raw = response.choices[0].message.content.strip()
    result = json.loads(raw)
    return result


def classify_tickets(messages: list) -> list:
    """
    Classify a list of support messages.
    Returns a list of dicts with message, category, and priority.
    """
    results = []

    for message in messages:
        try:
            classification = classify_message(message)
            results.append({
                "message": message,
                "category": classification.get("category", "Unknown"),
                "priority": classification.get("priority", "Unknown")
            })
        except json.JSONDecodeError:
            print(f"[ERROR] Could not parse JSON for message: {message}")
            results.append({
                "message": message,
                "category": "Error",
                "priority": "Error"
            })
        except Exception as e:
            print(f"[ERROR] API call failed for message: {message} | Reason: {str(e)}")
            results.append({
                "message": message,
                "category": "Error",
                "priority": "Error"
            })

    return results


if __name__ == "__main__":
    # Sample input messages
    messages = [
        "My payment got deducted but service is not activated",
        "App crashes every time I login",
        "How to change my email address?",
        "I was charged twice for the same subscription",
        "I cannot reset my password",
        "What are your business hours?"
    ]

    print("Classifying support tickets...\n")
    output = classify_tickets(messages)

    print(json.dumps(output, indent=2))

    # Save to output file
    with open("output.json", "w") as f:
        json.dump(output, f, indent=2)

    print("\nResults saved to output.json")
