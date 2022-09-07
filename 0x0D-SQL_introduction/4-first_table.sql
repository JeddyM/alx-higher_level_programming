-- creates a table called first_table in the current database
-- if the table first_table already exists, your script should not fail
-- SELECT or SHOW statements not allowed
CREATE TABLE IF NOT EXISTS first_table(id INT, name VARCHAR(256));
