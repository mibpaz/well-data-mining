CREATE SEQUENCE seq_well_id START 1;

CREATE SEQUENCE seq_log_type_id START 1;

CREATE SEQUENCE seq_logical_file_id START 1;

CREATE SEQUENCE seq_channel_id START 1;

CREATE SEQUENCE seq_reading_id START 1;

CREATE TABLE IF NOT EXISTS well (
    id INTEGER PRIMARY KEY DEFAULT nextval ('seq_well_id'),
    name VARCHAR(255) NOT NULL UNIQUE,
);

CREATE TABLE IF NOT EXISTS log_type (
    id INTEGER PRIMARY KEY DEFAULT nextval ('seq_log_type_id'),
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS logical_file (
    id INTEGER PRIMARY KEY DEFAULT nextval ('seq_logical_file_id'),
    well_id INT REFERENCES well (id) NOT NULL,
    log_type_id INT REFERENCES log_type (id) NOT NULL,
    name VARCHAR(255) NOT NULL,
    index_type VARCHAR(50) NOT NULL,
);

CREATE TABLE IF NOT EXISTS channel (
    id INTEGER PRIMARY KEY DEFAULT nextval ('seq_channel_id'),
    name VARCHAR(255) NOT NULL,
    unit VARCHAR(50) NOT NULL,
    UNIQUE (name, unit)
);

CREATE TABLE IF NOT EXISTS reading (
    id INTEGER PRIMARY KEY DEFAULT nextval ('seq_reading_id'),
    logical_file_id INT REFERENCES logical_file (id) NOT NULL,
    channel_id INT REFERENCES channel (id) NOT NULL,
    index_value FLOAT,
    reading_value VARCHAR(255)
);

CREATE INDEX IF NOT EXISTS idx_logical_file_well ON logical_file (well_id);

CREATE INDEX IF NOT EXISTS idx_logical_file_log_type ON logical_file (log_type_id);

CREATE INDEX IF NOT EXISTS idx_reading_lookup ON reading (
    logical_file_id,
    channel_id,
    index_value
);