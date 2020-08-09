#!/usr/bin/python3
"""
This will list all the states in the states SQL table
"""


def main():

    """ Only prints state if it matches the name searched for """
    import sys
    import MySQLdb
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{}' ORDER BY id ASC"
                .format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    """ This bit keeps it from executing when imported """
    main()
