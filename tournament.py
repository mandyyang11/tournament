#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname=tournament")
        cursor = db.cursor()
        return db, cursor
    except:
        print "Can not connect to the tournament database"


def deleteMatches():
    """Remove all the match records from the database."""
    conn, c = connect()
    c.execute("DELETE FROM matches;")
    conn.commit()
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn, c = connect()
    c.execute("DELETE FROM players;")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn, c = connect()
    c.execute("SELECT COUNT(*) FROM players;")
    return c.fetchone()[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn, c = connect()
    c.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # place all players in a dictionary
    player_dict = {}
    conn, c = connect()
    c.execute("""SELECT * FROM players;""")
    for row in c.fetchall():
        player_dict[row[0]] = [row[1], 0, 0]

    # count the number of win and matches in for all matches
    c.execute("""SELECT winner, loser FROM matches;""")
    for row in c.fetchall():
        if row[0] in player_dict:
            player_dict[row[0]][1] += 1
            player_dict[row[0]][2] += 1
        if row[1] in player_dict:
            player_dict[row[1]][2] += 1

    # compile win counts as the key to dictionary
    win_count = {}
    for i in player_dict:
        wins = player_dict[i][1]
        if wins in win_count:
            win_count[wins].append((i, player_dict[i][0],
                                    wins, player_dict[i][2]))
        else:
            win_count[wins] = [(i, player_dict[i][0],
                                wins, player_dict[i][2])]

    # compile output list
    output_list = []
    for i in sorted(win_count.keys(), reverse=True):
        for j in win_count[i]:
            output_list.append(j)

    return output_list


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn, c = connect()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s);",
              (winner, loser,))
    conn.commit()
    conn.close()

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    player_list = playerStandings()
    match_list = []

    # assume its always even
    for i in xrange(0, len(player_list), 2):
        id1, name1, wins1, matches1 = player_list[i]
        id2, name2, wins2, matches2 = player_list[i+1]
        match_list.append((id1, name1, id2, name2))
    return match_list

