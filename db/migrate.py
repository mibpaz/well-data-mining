import sqlite3

# Define your file paths
sql_file_path = "db/migration.sql"
database_path = "db/volve.db"

try:
    with open(sql_file_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    with sqlite3.connect(database_path) as conn:
        cursor = conn.cursor()

        cursor.executescript(sql_script)

        conn.commit()

    print(f"Database '{database_path}' created successfully from '{sql_file_path}'.")

except sqlite3.Error as e:
    print(f"An SQLite error occurred: {e}")
except FileNotFoundError:
    print(f"Error: The file '{sql_file_path}' was not found.")
