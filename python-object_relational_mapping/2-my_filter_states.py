#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(user=user, passwd=password, db=db_name, host='localhost', port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
