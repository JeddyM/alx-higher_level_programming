#!/usr/bin/python3
'''takes in the name of a state as an argument and lists all cities
of that state using the database hbtn_0e_4_usa
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # making connecting
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])

    # Creating cursor
    cur = conn.cursor()

    # query
    cur.execute("SELECT cities.name FROM cities JOIN states ON\
                cities.state_id = states.id AND states.name = %s\
                ORDER BY cities.id ASC ", (argv[4], ))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
