-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


\c tournament

DROP TABLE IF EXISTS players;
CREATE TABLE players (
	ID SERIAL PRIMARY KEY,
	name VARCHAR(100) DEFAULT NULL
);

DROP TABLE IF EXISTS matches;
CREATE TABLE matches (
	winner INTEGER REFERENCES players(ID),
	loser INTEGER REFERENCES players(ID),
	PRIMARY KEY (winner, loser)
);
