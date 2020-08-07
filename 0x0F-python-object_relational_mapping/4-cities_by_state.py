#!/usr/bin/python3
"""
This will list all the states in the states SQL table
"""


def main():

    """ Prints cities """
    import sys
    import MySQLdb
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    str1 = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN"
    str2 = " states ON cities.state_id = states.id ORDER BY cities.id ASC;"
    cur.execute(str1 + str2)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    """ This bit keeps it from executing when imported """
    main()
