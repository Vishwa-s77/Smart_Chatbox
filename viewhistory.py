import mysql.connector
def view_chat_history():
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
        password = input("🔒 Enter password: ").strip()

        # First authenticate user
        cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
            # Fetch chat history
            cursor.execute("""
                SELECT message, response, timestamp
                FROM chat_history
                WHERE user_id = %s
                ORDER BY timestamp
            """, (user_id,))
            chats = cursor.fetchall()

            if chats:
                print(f"\n📜 Chat history for {username}:")
                for idx, (message, response, timestamp) in enumerate(chats, 1):
                    print(f"\n🔹 Chat {idx}:")
                    print(f"   🧑 You: {message}")
                    print(f"   🤖 Bot: {response}")
                    print(f"   🕰️ Time: {timestamp}")
            else:
                print(f"\n ⚠️ No chat history found for {username}.")
        else:
            print("❌ Invalid username or password.")

    except mysql.connector.Error as e:
        print("❌ Database Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
