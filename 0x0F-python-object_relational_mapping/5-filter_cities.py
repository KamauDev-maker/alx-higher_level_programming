#!/usr/bin/python3
"""
 a script that takes in the name of a state as
 an argument and lists all cities of that state,
 using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            state_name=sys.argv[4])
    cur = db.cursor()
    query = """SELECT cities.name FROM cities
           JOIN states ON cities.state_id = states.id
           WHERE states.name = %s
           ORDER BY cities.id ASC"""
    cur.execute(query, (state_name,))
    results = cur.fetchall()
    print(", ".join(city[0] for city in results))

    cur.close()
    db.close()
