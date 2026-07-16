CREATE TABLE IF NOT EXISTS well (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS log_type (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS logical_file (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    well_id INT REFERENCES well (id) ON DELETE CASCADE NOT NULL,
    log_type_id INT REFERENCES log_type (id) ON DELETE CASCADE NOT NULL,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS channel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    unit VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (name, unit)
);

CREATE TABLE IF NOT EXISTS reading (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    logical_file_id INT REFERENCES logical_file (id) ON DELETE CASCADE NOT NULL,
    channel_id INT REFERENCES channel (id) ON DELETE CASCADE NOT NULL,
    index_value FLOAT,
    reading_value FLOAT
);

CREATE INDEX IF NOT EXISTS idx_logical_file_well ON logical_file (well_id);

CREATE INDEX IF NOT EXISTS idx_logical_file_log_type ON logical_file (log_type_id);

CREATE INDEX IF NOT EXISTS idx_reading_lookup ON reading (
    logical_file_id,
    channel_id,
    index_value
);