-- Creates a new user user_0d_1 and grant all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH 'user_0d_1_pwd';
-- Grant all privileges to new user
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
