#!/usr/bin/python3
""" same as task 2, but safe from sql injections """


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute(
        "SELECT * \
        FROM  states WHERE BINARY name=%s \
        ORDER BY id ASC",(sys.argv[4],)
    )

    result = cur.fetchall()

    for row in result:
        print(row)
