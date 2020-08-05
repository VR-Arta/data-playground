CREATE TABLE users (id INT PRIMARY KEY, name TEXT, age INT);
CREATE INDEX idx_users_age ON users(age);
