#!/usr/bin/python3
"""Lists all states from the hbtn_0e_0_usa database"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    name_match = sys.argv[4]
    cur.execute("""SELECT cities.name
                FROM cities INNER JOIN states ON
                states.id=cities.state_id
                WHERE states.name=%s
                ORDER BY cities.id""", (name_match,))
    rows = cur.fetchall()
    for row in rows:
        print(row[0], sep=", ")
    cur.close()
    db.close()
