from pathlib import Path
import duckdb

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "volve.duckdb"
MIGRATION_PATH = BASE_DIR / "migration.sql"

# --- Migration Script Executer ---
sql_file_path = "db/migration.sql"
database_path = str(DB_PATH)

try:
    with open(sql_file_path, "r", encoding="utf-8") as file:
        sql_script = file.read()

    with duckdb.connect(database_path) as conn:
        conn.execute(sql_script)

    print(f"Database '{database_path}' created successfully from '{sql_file_path}'.")

except duckdb.Error as e:
    print(f"A DuckDB error occurred: {e}")
except FileNotFoundError:
    print(f"Error: The file '{sql_file_path}' was not found.")
