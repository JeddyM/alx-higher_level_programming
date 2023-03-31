#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''

import MySQLdb
from sys import argv


# making connecting
conn = MySQLdb.connect(host="localhost",port=3306, user=argv[1], passwd=argv[2], db=argv[3])

# Creating cursor
cur = conn.cursor()

# query
cur.execute("SELECT * FROM states ORDER BY id ASC")
rows = cur.fetchall()
for i in rows:
    print(i)
cur.close()
conn.close()
#if __name__ == '__main__':
 #   main()

