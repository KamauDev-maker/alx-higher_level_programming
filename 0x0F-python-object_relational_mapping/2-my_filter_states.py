#!/usr/bin/python3
"""takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE"
        "'{:s}' ORDER BY id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if i[1] == sys.argv[4]:
            print(row)
