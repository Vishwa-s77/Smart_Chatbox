import mysql.connector
from mysql.connector import Error


try:
    # Step 1: Connect to the DB
    connection = mysql.connector.connect(
        host='localhost',
        port=3309,
        user='root',
        password='tiger@12345678',          # 🔐 Replace with your MySQL password
        database='chatbot_db'              # 🧠 Replace with your DB name
    )

    if connection.is_connected():
        print(" Connected to MySQL 8.0")

        cursor = connection.cursor()

        # Step 2: Create a table (if not exists)
        create_table_query = """
        CREATE TABLE IF NOT EXISTS chat_history (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT,
            response TEXT
        )
        """
        cursor.execute(create_table_query)
        print(" Table checked/created.")

        # Step 3: Insert test data
        insert_query = "INSERT INTO chat_history (user_id,message, response) VALUES (%s,%s, %s)"
        data = (777,"Doomyy", "Glad brother!")
        cursor.execute(insert_query, data)
        connection.commit()
        print(" Test data inserted.")

        # Step 4: Read data
        cursor.execute("SELECT * FROM chat_history")
        rows = cursor.fetchall()
        print("\n Chat History:")
        for row in rows:
            print(row)

except Error as e:
    print(" Error:", e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print(" MySQL connection closed.")
