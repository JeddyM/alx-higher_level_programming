-- script that creates the database hbtn_0d_usa and the table cities
-- description id INT unique, auto generated, not null & is primary key
-- state_id INT, not null, must be FOREIGN KEY that references to id of states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
        id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(256) NOT NULL,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
        );
