from pathlib import Path
import duckdb
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "volve.duckdb"

con = duckdb.connect(str(DB_PATH))
cur = con.cursor()


def _insert(table, columns, values):
    """Inserts a single row and instantly returns its ID using standard SQL RETURNING"""
    placeholders = ", ".join("?" for _ in values)
    column_names = ", ".join(columns)
    query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders}) RETURNING id"

    result = cur.execute(query, list(values)).fetchone()
    return result[0] if result else None


def bulk_insert_readings(df: pd.DataFrame):
    if df.empty:
        return

    cur.execute(
        "INSERT INTO reading (logical_file_id, channel_id, index_value, reading_value) SELECT * FROM df"
    )


def remove(table, condition_column, condition_value):
    query = f"DELETE FROM {table} WHERE {condition_column} = ?"
    cur.execute(query, [condition_value])


def create(table, data: dict):
    return _insert(table, list(data.keys()), list(data.values()))


def update(table, record_id, data: dict):
    set_clause = ", ".join(f"{key} = ?" for key in data.keys())
    query = f"UPDATE {table} SET {set_clause} WHERE id = ?"
    cur.execute(query, list(data.values()) + [record_id])


def find(table, channel_name, unit):
    query = f"SELECT id FROM {table} WHERE name = ? AND unit = ?"
    cur.execute(query, [channel_name, unit])
    result = cur.fetchone()
    return result[0] if result else None


def find_or_create(table, data):
    where_clause = " AND ".join(f"{key} = ?" for key in data.keys())
    query = f"SELECT id FROM {table} WHERE {where_clause}"

    cur.execute(query, list(data.values()))
    result = cur.fetchone()

    if result:
        return result[0]
    else:
        return _insert(table, list(data.keys()), list(data.values()))


def close():
    cur.close()
    con.close()


db = {
    "find_or_create": find_or_create,
    "find": find,
    "update": update,
    "create": create,
    "remove": remove,
    "bulk_insert_readings": bulk_insert_readings,
    "close": close,
}
