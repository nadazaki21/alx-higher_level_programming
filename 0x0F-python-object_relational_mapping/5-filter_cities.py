#!/usr/bin/python3
"""  script that takes in the name of a state as an
argument and lists all cities of that state,
using the database hbtn_0e_4_usa """


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute(
        "SELECT name FROM cities WHERE state_id= \
        (SELECT id from states WHERE name='{}') \
        ORDER BY id ASC ".format(
            sys.argv[4]
        )
    )

    result = cur.fetchall()

    cities = [tup[0] for tup in result]
    cities_str = ", ".join(cities)
    print(cities_str)
