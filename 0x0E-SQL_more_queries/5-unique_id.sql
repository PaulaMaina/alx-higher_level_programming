-- Creates the table unique_id
CREATE TABLE IF NOT EXISTS unique_id (
	id int UNIQUE DEFAULT 1,
	name varchar(256)
);
