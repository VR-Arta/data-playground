CREATE TABLE users (id INT PRIMARY KEY, name TEXT, age INT);
CREATE INDEX idx_users_age ON users(age);
CREATE INDEX idx_users_name ON users(name);
