from pathlib import Path
import sqlite3
from models import LogicalFile, Channel, Reading

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "volve.db"
MIGRATION_PATH = BASE_DIR / "migration.sql"

con = sqlite3.connect(DB_PATH, timeout=30)
cur = con.cursor()
cur.execute("PRAGMA busy_timeout = 30000")
cur.execute("PRAGMA foreign_keys = ON")


def _insert(table, columns, values):
    placeholders = ", ".join("?" for _ in values)
    column_names = ", ".join(columns)
    query = f"INSERT INTO {table} ({column_names}) VALUES ({placeholders})"
    cur.execute(query, values)
    return cur.lastrowid


def remove(table, condition_column, condition_value):
    query = f"DELETE FROM {table} WHERE {condition_column} = ?"
    cur.execute(query, (condition_value,))
    con.commit()


def create_log_type(name):
    log_type_id = _insert("log_type", ["name"], [name])
    con.commit()
    return log_type_id


def create_well(name):
    well_id = _insert("well", ["name"], [name])
    con.commit()
    return well_id


def create_file(well_id, data: LogicalFile):
    file_id = _insert("logical_file", data.keys(), data.values())
    con.commit()
    return file_id


def create_channel(data: Channel):
    channel_id = _insert("channel", data.keys(), data.values())
    con.commit()
    return channel_id


def create_reading(well_id, data: Reading):
    reading_id = _insert("reading", data.keys(), data.values())
    con.commit()
    return reading_id


def create(table, data: dict):
    record_id = _insert(table, data.keys(), data.values())
    con.commit()
    return record_id


def update(table, record_id, data: dict):
    set_clause = ", ".join(f"{key} = ?" for key in data.keys())
    query = f"UPDATE {table} SET {set_clause} WHERE id = ?"
    cur.execute(query, (*data.values(), record_id))
    con.commit()


def find(table, channel_name, unit):
    query = f"SELECT id FROM {table} WHERE name = ? AND unit = ?"
    cur.execute(query, (channel_name, unit))
    result = cur.fetchone()
    return result[0] if result else None


def find_or_create(table, data):
    fields = ", ".join(data.keys())
    query = f"SELECT id FROM {table} WHERE {fields}"
    cur.execute(query, tuple(data.values()))
    result = cur.fetchone()

    if result:
        return result[0]
    else:
        # If the file doesn't exist, create it
        return _insert(table, list(data.keys()), list(data.values()))


def close_connection():
    con.close()


db = {
    "create_well": create_well,
    "create_file": create_file,
    "create_channel": create_channel,
    "create_reading": create_reading,
    "close_connection": close_connection,
    "create_log_type": create_log_type,
    "create": create,
    "update": update,
    "remove": remove,
    "find": find,
    "find_or_create": find_or_create,
}
