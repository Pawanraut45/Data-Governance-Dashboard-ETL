-- sql/create_tables.sql
CREATE TABLE IF NOT EXISTS transactions (
tx_id INTEGER PRIMARY KEY,
user_id INTEGER,
amount NUMERIC,
currency TEXT,
created_at TIMESTAMP,
email TEXT
);


CREATE TABLE IF NOT EXISTS transactions_curated AS SELECT * FROM transactions WHERE 1=0;