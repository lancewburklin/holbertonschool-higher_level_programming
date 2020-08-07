#!/usr/bin/python3
"""
This will list all the states in the states SQL table
"""


def main():

    """ Prints cities by state """
    import sys
    import MySQLdb
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    str1 = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN"
    str2 = " states ON cities.state_id = states.id ORDER BY cities.id ASC;"
    cur.execute(str1 + str2)
    query_rows = cur.fetchall()
    first_time = 0
    cities = ""
    for row in query_rows:
        if first_time != 0 and row[2] == sys.argv[4]:
            cities = cities + ", "
        if row[2] == sys.argv[4]:
            first_time = 1
            cities = cities + str(row[1])
    print(cities)
    cur.close()
    conn.close()

if __name__ == "__main__":
    """ This bit keeps it from executing when imported """
    main()
