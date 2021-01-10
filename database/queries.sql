SELECT name, age FROM users WHERE age > 25;
SELECT COUNT(*) FROM users;
SELECT department, COUNT(*) AS total_users FROM users GROUP BY department;
