-- Creates a new user user_0d_1
-- Sets the user's password to 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH 'user_0d_1_pwd';
-- Grant all privileges to the new user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
