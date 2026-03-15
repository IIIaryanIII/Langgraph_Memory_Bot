# LangGraph Memory Bot 🧠🤖

An AI chatbot built using **LangGraph**, **Gemini (Google Generative AI)**, and **MongoDB** that can **remember conversations across sessions** using checkpoint-based memory.

This project demonstrates how to build a **stateful AI agent** with persistent memory using LangGraph's checkpointing system.

---

## 🚀 Features

* 🤖 AI Chatbot powered by **Gemini 2.5 Flash**
* 🧠 **Persistent memory** using **LangGraph Checkpoints**
* 💾 **MongoDB storage** for conversation history
* 🔄 **Thread-based memory** using `thread_id`
* 🐳 **Docker support** for MongoDB
* ⚡ Streaming responses using LangGraph

---

## 🏗️ Tech Stack

* **LangGraph**
* **LangChain**
* **Google Gemini API**
* **MongoDB**
* **Docker**
* **Python**

---

## 📂 Project Structure

```
Langgraph_Memory_Bot
│
├── chat.py                # Basic chatbot
├── chat_2.py              # LangGraph workflow example
├── chat_checkpoint.py     # Chatbot with MongoDB memory
├── docker-compose.yml     # MongoDB container setup
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not pushed to GitHub)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/Langgraph_Memory_Bot.git
cd Langgraph_Memory_Bot
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add environment variables

Create a `.env` file:

```
GOOGLE_API_KEY=your_gemini_api_key
```

---

### 5️⃣ Start MongoDB using Docker

```
docker compose up -d
```

This starts a MongoDB container on:

```
mongodb://admin:admin@localhost:27017
```

---

### 6️⃣ Run the chatbot

```
python chat_checkpoint.py
```

---

## 🧠 How Memory Works

The chatbot stores conversation history in **MongoDB** using LangGraph checkpoints.

Each conversation is associated with a **thread_id**:

```
config = {
  "configurable": {
      "thread_id": "Aryan"
  }
}
```

This allows the chatbot to **remember previous interactions across sessions**.

Example:

```
User: Hey I am Aryan
Bot: Nice to meet you Aryan!

User: What is my name?
Bot: Your name is Aryan.
```

---

## 📸 Example Output

```
User: Hey I am Aryan
Bot: Hi Aryan! Nice to meet you.

User: What is my name?
Bot: Your name is Aryan.
```

---

## 🛠️ Future Improvements

* Web UI for chatting
* FastAPI backend
* Tool usage (calculator, search APIs)
* Multi-agent workflows
* Long-term memory summarization

---

## 👨‍💻 Author

Aryan

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
