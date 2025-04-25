import chatbot_engine as ch
import mysql.connector
import viewhistory as vs

# 🔐 Register user if not exists
def register_user(cursor, connection, username, password):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        connection.commit()
        cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
        result = cursor.fetchone()
        print("🆕 New user registered!")
        return result[0]
    except mysql.connector.Error as e:
        print("❌ Registration failed:", e)
        return None

# 🔑 Login or register user
def authenticate_user():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3309,
            user='root',
            password='tiger@12345678',
            database='chatbot_db'
        )
        cursor = connection.cursor()

        username = input("👤 Enter username: ").strip()
        password = input("🔐 Enter password: ").strip()

        cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()

        if result:
            print("✅ Login successful!")
            return result[0]
        else:
            print("❌ Invalid username or password.")
            choice = input("🆕 Do you want to register as a new user? (yes/no): ").strip().lower()
            if choice == 'yes':
                return register_user(cursor, connection, username, password)
            else:
                return None

    except mysql.connector.Error as e:
        print("❌ Database Error:", e)
        return None

# 🚀 Run the chatbot
def run_chatbot():
    user_id = authenticate_user()
    if not user_id:
        print("🔒 Exiting... You must login or register to continue.")

    while True:
        user_input = input("👤 You: ").strip()

        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break

        bot_reply = ch.get_bot_response(user_input)
        print(f"🤖 Bot: {bot_reply}")
        ch.save_to_db(user_id, user_input, bot_reply)

# 🎯 Entry point
if __name__ == "__main__":
    while True:
        print("\n📋 Menu:")
        print("1. Chat with Bot")
        print("2. View Chat History")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            run_chatbot()
        elif choice == '2':
           vs.view_chat_history()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please select 1, 2, or 3.")
