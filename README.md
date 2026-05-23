# 🎫 AI Support Ticket Classifier

An AI-powered solution that automatically classifies customer support messages by **category** and **priority** using an AI API.

> ⚠️ **Note:** This project was built using the **Groq API** (LLaMA 3.3 model) as a free alternative to OpenAI, due to billing restrictions on the free tier. Groq follows the exact same API format as OpenAI. Switching to OpenAI requires changing only 2 lines of code. The logic, prompt engineering, error handling, and JSON output remain completely identical.

---

## 📌 Problem Statement

Customer support teams receive a high volume of messages daily. Manually reading and categorizing each one is inefficient and error-prone. This tool uses OpenAI to automate classification and prioritization — saving time and reducing human error.

---

## ⚙️ How It Works

1. You provide a list of customer messages
2. Each message is sent to OpenAI's API with a structured prompt
3. The model classifies it into a **category** and **priority**
4. Results are returned as clean **JSON**

---

## 🗂️ Categories

| Category | Description |
|---|---|
| Billing | Payment, charges, subscription issues |
| Technical Issue | Bugs, crashes, errors |
| Account | Login, password, profile changes |
| General Inquiry | General questions, information requests |

## 🚨 Priority Levels

| Priority | When to use |
|---|---|
| High | Urgent or blocking issues |
| Medium | Moderate issues |
| Low | General or informational queries |

---

## 🚀 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/roshankumars0205/support-ticket-classifier.git
cd support-ticket-classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API Key
```bash
# On Mac/Linux
export OPENAI_API_KEY="your-api-key-here"

# On Windows
set OPENAI_API_KEY="your-api-key-here"
```

### 4. Run the classifier
```bash
python classifier.py
```

---

## 📥 Input Format

Edit the `messages` list inside `classifier.py`:

```python
messages = [
    "My payment got deducted but service is not activated",
    "App crashes every time I login",
    "How to change my email address?"
]
```

---

## 📤 Sample Output

```json
[
  {
    "message": "My payment got deducted but service is not activated",
    "category": "Billing",
    "priority": "High"
  },
  {
    "message": "App crashes every time I login",
    "category": "Technical Issue",
    "priority": "High"
  },
  {
    "message": "How to change my email address?",
    "category": "Account",
    "priority": "Low"
  }
]
```

Results are also saved automatically to `output.json`.

---

## 🛡️ Error Handling

- Invalid JSON responses from API are caught and logged
- API failures are handled gracefully — the script continues with remaining messages
- Each failed message is returned with `"Error"` status instead of crashing

---

## 🧰 Tech Stack

- **Python 3.13** (via Anaconda)
- **Groq API** (`llama-3.3-70b-versatile`) — free alternative to OpenAI
- JSON for structured output

---

## 📁 Project Structure

```
support-ticket-classifier/
├── classifier.py      # Main script
├── requirements.txt   # Dependencies
├── output.json        # Sample output
└── README.md          # This file
```
