import mysql.connector
from datetime import datetime
import google.generativeai as genai

# 🔐 Set your Gemini API key
genai.configure(api_key="XXX")  # Replace with your actual key

# 🤖 Get response from Gemini
def get_bot_response(user_input):
    if not user_input:
        return "You didn't say anything!"

    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")  # ✅ Correct model
        chat = model.start_chat()
        response = chat.send_message(user_input)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error from Gemini: {e}"
# 💾 Save chat to MySQL
def save_to_db(user_id, message, response):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3309,
            user='root',
            password='tiger@12345678',
            database='chatbot_db'
        )
        cursor = connection.cursor()

        query = """
        INSERT INTO chat_history (user_id, message, response, timestamp)
        VALUES (%s, %s, %s, %s)
        """
        timestamp = datetime.now()
        cursor.execute(query, (user_id, message, response, timestamp))
        connection.commit()
        print("💾 Chat saved to database.")

    except mysql.connector.Error as e:
        print("❌ Database Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()