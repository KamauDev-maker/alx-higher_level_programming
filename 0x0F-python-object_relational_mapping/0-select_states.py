#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa takes 3 arguments
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Database credentials

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=dbname,
            port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT *FROM states ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
