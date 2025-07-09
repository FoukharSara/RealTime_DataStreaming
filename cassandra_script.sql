CREATE KEYSPACE IF NOT EXISTS user_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE user_keyspace;

CREATE TABLE IF NOT EXISTS users (
    email TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    gender TEXT,
    address TEXT,
    post_code TEXT,
    username TEXT,
    dob TEXT,
    registered_date TEXT,
    phone TEXT,
    picture TEXT
);