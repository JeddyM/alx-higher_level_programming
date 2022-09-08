-- Creates the database hbtn_0d_2 and the user user_0d_2
-- user has only SELECT privilege
-- if db exists script should not fail
-- if user already exits script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2 IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
