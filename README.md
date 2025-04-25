🧠 Smart Chatbot with Memory
A Python-based chatbot powered by Google Gemini AI, with MySQL database integration to remember conversations and manage users securely.
Users can register, login, and view their personal chat history anytime!

✨ Features:
🔐 User Authentication (username + password)
2.🆕 User Registration if not already registered
3.🤖 AI-powered responses using Google Gemini 1.5 Pro
4.💾 Chat history storage in MySQL (with timestamps)
5.📜 View conversation history based on user login
6.⚙️ Error handling for database and API errors


🛠️ Tech Stack:
1.Python 3.x
2.Google Generative AI (gemini-1.5-pro via API)
3.MySQL 8.0+
4.mysql-connector-python
5.Git & GitHub

🏗️ Project Structure:
Smart Chatbot with Memory/
│
├── main.py               # Entry point - handles login/register/chat loop
├── chatbot_engine.py      # Handles Gemini API communication and DB saving
├── db_manager.py          # Manages DB connections, user auth, and user registration
├── README.md              # Project documentation (this file)
└── __pycache__/           # Python cache (auto-generated)

