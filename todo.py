# Todo App - CRUD Operations (Create, Read, Update, Delete)
# Steps:
# 1. Check Python version: python -V
# 2. Check installed packages: pip list
# 3. Install MySQL connector: pip install mysql-connector-python
# 4. Establish database connection & perform CRUD on tasks

import mysql.connector as mysql

# Establishing the connection
db = mysql.connect(host="localhost", user="root", passwd="root")
cur = db.cursor()

# Create database if it doesn't exist
cur.execute("CREATE DATABASE IF NOT EXISTS TODOAPP")

# Switch to the created database
cur.execute("USE TODOAPP")

# Create table for tasks
cur.execute("""
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(100) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")
print("✅ Table ready!")

# Display existing tables (for verification)
cur.execute("SHOW TABLES")
for tbl in cur.fetchall():
    print("Table found:", tbl[0])

# Application Menu
while True:
    print("\n--- TODO Application ---")
    print("1. Create Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Quit")

    user_choice = input("Select an option: ")

    if user_choice == "1":
        task_input = input("Enter the task description: ")
        cur.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task_input,))
        db.commit()
        print("📝 New task added!")

    elif user_choice == "2":
        cur.execute("SELECT * FROM tb_todo")
        tasks = cur.fetchall()
        print("\n--- Task List ---")
        for row in tasks:
            print(f"ID: {row[0]}, Task: {row[1]}, Status: {row[2]}")
    
    elif user_choice == "3":
        task_id = input("Enter Task ID to update: ")
        new_status = input("Enter new status (pending/completed): ")
        cur.execute("UPDATE tb_todo SET status=%s WHERE id=%s", (new_status, task_id))
        db.commit()
        print("✅ Task updated successfully!")

    elif user_choice == "4":
        task_id = input("Enter Task ID to delete: ")
        cur.execute("DELETE FROM tb_todo WHERE id=%s", (task_id,))
        db.commit()
        print("🗑️ Task deleted!")

    elif user_choice == "5":
        print("👋 Exiting the application...")
        break

    else:
        print("⚠️ Invalid option! Please choose between 1-5.")

# Closing connection
cur.close()
db.close()
