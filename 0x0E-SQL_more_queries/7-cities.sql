-- Creates database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Uses the created database
USE `hbtn_0d_usa`;
-- Creates the table cities if it does not exist
CREATE TABLE IF NOT EXISTS cities (
	id int UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id int NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id),
	name varchar(256)
);
