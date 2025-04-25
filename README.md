# 🧠 Smart Chatbot with Memory  
A Python-based chatbot powered by **Google Gemini AI**, with secure MySQL integration to **remember conversations**, handle **user login/registration**, and provide a personalized chat experience.

Users can **register**, **log in**, and view their **individual chat histories** anytime — your AI assistant now remembers!

---

## ✨ Features

- 🔐 **User Authentication** with username and passwords  
- 🆕 **User Registration** for new users  
- 🤖 **AI-powered Conversations** using **Google Gemini 1.5 Pro**  
- 💾 **Chat History Storage** in MySQL with timestamp tracking  
- 📜 **Conversation History Viewer** filtered by authenticated users  
- ⚙️ Robust **error handling** for both DB and API failures  

---

## 🤖 Gemini AI Integration

This project uses **Google Generative AI’s `gemini-1.5-pro` model** for powerful, real-time chatbot interactions.  
The chatbot intelligently responds to user input while maintaining context per session.

```python
model = genai.GenerativeModel(model_name="gemini-1.5-pro")
chat = model.start_chat()
response = chat.send_message(user_input)


 ## 🛠️ Tech Stack:

-Python 3.x
-Google Generative AI (gemini-1.5-pro via API)
-MySQL 8.0+
-mysql-connector-python
-Git & GitHub

 ## 🏗️ Project Structure:
-Smart Chatbot with Memory/
-│
-├── main.py               # Entry point - handles login/register/chat loop
-├── chatbot_engine.py      # Handles Gemini API communication and DB saving
-├── db_manager.py          # Manages DB connections, user auth, and user registration
-├── README.md              # Project documentation (this file)
-└── __pycache__/           # Python cache (auto-generated)

