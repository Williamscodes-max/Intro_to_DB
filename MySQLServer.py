import mysql.connector

try:
    # Connect to MySQL server (without specifying a database)
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password"
    )

    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()
