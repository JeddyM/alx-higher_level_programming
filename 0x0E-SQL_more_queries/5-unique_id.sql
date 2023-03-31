-- creates the table unique_id
-- Description id INT with the default value 1 must be uniques
-- name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
	);
