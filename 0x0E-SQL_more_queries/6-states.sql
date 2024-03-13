-- Creates database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- Creates the table states if it does not exist
CREATE TABLE IF NOT EXISTS states (
	id int UNIQUE AUTO_INCREMENT NOT NULL PRIMARY_KEY,
	name varchar(256)
);
