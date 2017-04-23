# Tournaments
## Description
This project works with PostgreSQL database to setup a database of tournament and generate
the matches with swiss pairings.

## Whats included?
Tournament Project
- tournament.sql
- tournament.py
- tournament_test.py

### tournament.sql
This sql file sets up a tournament database schema with tables like players and matches.

### tournament.py
This python file contains methods to connect, read, add, delete players and matches as 
well as generate match parings with swiss rule.

### tournament_test.py
This python file has scripts to test the methods implemented in tournament.py file.

## How to setup environment?
Fillow the guidelines probvided in the [project description](https://docs.google.com/document/d/16IgOm4XprTaKxAa8w02y028oBECOoB1EI1ReddADEeY/pub?embedded=true) 
to set up the vagran vm, Virtual Box, and clone [fullstack-nanodegree-vm repository](https://www.google.com/url?q=http://github.com/udacity/fullstack-nanodegree-vm&sa=D&ust=1475465670158000&usg=AFQjCNFiTqmx6MLxiP7X8G2m9lMExxrPBA).
Replace attached `tournament.sql`, `tournament.py`, and `tournament_test.py` with 
the ones in `<path to your local fullstack-nanodegree-vm repository>/vargant/tournament`.

## How to execute tests?
After following the guidelines in project description and setting up the environment, use the following instructions in the Terminal.

0. Change the working directory with `cd <path to your local vagrant directory>`
1. Power on virtual machine with `vagrant up`
2. Log into the virtual machine with `vagrant ssh`
3. Change directory to the synced folder with `cd /vagrant`
4. Lunches PostgreSQL with `psql`
5. Create tournament database with `CREATE DATABASE tournament;`
6. Create tables with `\i tournament.sql`
7. Quit PostgreSQL with `\q`
8. Run tests with `python tournament_test.py`
9. Test results will be printed on the screen



