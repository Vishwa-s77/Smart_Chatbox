# 🧠 Smart Chatbot with Memory

A Python-based chatbot powered by **Google Gemini AI**, with **MySQL** integration to remember conversations and manage users securely. Users can **register**, **login**, and **view their personal chat history**—all from the terminal!

---

## ✨ Features

- 🔐 **User Authentication** (username + password)
- 🆕 **User Registration** if not already registered
- 🤖 **AI-powered responses** using Gemini 1.5 Pro
- 💾 **Chat history storage** in MySQL with timestamps
- 📜 **View conversation history** based on user login
- ⚙️ **Error handling** for database and API failures

---

## 🛠️ Tech Stack

- 🐍 Python 3.x  
- 🧠 Google Generative AI (`gemini-1.5-pro`)  
- 🐬 MySQL 8.0+  
- 🔌 `mysql-connector-python`  
- 🌐 Git & GitHub  

---

## 🗂️ Project Structure

Smart Chatbot with Memory/ │ ├── main.py # 🎯 Main logic: handles user login/register and chat loop ├── chatbot_engine.py # 🧠 Gemini API integration + DB save logic ├── db_manager.py # 🗄️ DB setup, user auth, registration ├── templates/ │ └── index.html # 🖥️ (Optional) HTML frontend for future use ├── README.md # 📘 This file └── pycache/ # 🐍 Python cache files

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-chatbot-memory.git
cd smart-chatbot-memory
2. Install Dependencies
--bash
pip install mysql-connector-python google-generativeai

3. Set Up Your MySQL Database
Create a database:

CREATE DATABASE chatbot_db;
Create the required tables:
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  password VARCHAR(100) NOT NULL
);

CREATE TABLE chat_history (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  message TEXT,
  response TEXT,
  timestamp TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
Update MySQL connection config in db_manager.py.

4. Set Your Gemini API Key
In chatbot_engine.py, replace:

genai.configure(api_key="your-api-key-here")

5. Run the App
--bash
python main.py

####✅ Todo / Improvements
 Add web-based frontend for chat interface

 Add session-based memory using file or Redis

 Encrypt passwords using bcrypt for security

 Add admin panel for chat log monitoring

####📬 Contact
For suggestions, bugs, or collaboration — feel free to open an issue or submit a pull request.

Made with 💻 and ☕ by [Vishwas]

Let me know if you'd like me to insert your **actual GitHub URL** or your **name** in the contact section!