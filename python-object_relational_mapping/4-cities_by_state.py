#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(user=user, passwd=password, db=db_name, host='localhost', port=3306)
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        ORDER BY cities.id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
