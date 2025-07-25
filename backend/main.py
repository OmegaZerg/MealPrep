import sqlite3
from database_func import *
from constants import *

def main():
    print("Hello from backend!")
    con = sqlite3.connect("mealprep.db")
    cur = con.cursor()

    if not table_exists("foods", cur):
        cur.execute(CREATE_FOODS_TABLE)

    #Even though columns are not required, we must still provide data for every column when inserting. Any values we do not have will required defaults like "N/A"
    tables = cur.execute(SELECT_ALL_TABLES)
    print(tables.fetchall())
    cur.executemany("INSERT INTO foods VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", SAMPLE_FOODS)
    con.commit()

    for row in cur.execute(SELECT_ALL_FOODS):
        print(row)

    #print(cur.execute(SELECT_ALL_FOODS))

    con.close()

if __name__ == "__main__":
    main()
