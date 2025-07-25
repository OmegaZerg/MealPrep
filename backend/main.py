import sqlite3
from database_func import *
from constants import *

def main():
    print("Hello from backend!")
    con = sqlite3.connect("mealprep.db")
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    if not table_exists("foods", cur):
        cur.execute(CREATE_FOODS_TABLE)
        con.commit()
    if not table_exists("meals", cur):
        cur.execute(CREATE_MEALS_TABLE)
        con.commit()

    #Even though columns are not required, we must still provide data for every column when inserting. Any values we do not have will required defaults like "N/A"
    tables = cur.execute(SELECT_ALL_TABLES)
    print(tables.fetchall())

    #Testing foods
    # cur.executemany("INSERT INTO foods VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", SAMPLE_FOODS)
    # con.commit()

    #Testing meals
    # cur.executemany("INSERT INTO meals VALUES (?, ?, ?, ?, ?, ?, ?, ?)", SAMPLE_MEALS)
    # con.commit()

#     query = """
# DROP TABLE foods;
# """
#     cur.execute(query)
#     con.commit()

#     query = """
# DELETE FROM foods;
# """
#     cur.execute(query)
#     con.commit()
    print("Displaying all foods: ")
    for row in cur.execute(SELECT_ALL_FOODS):
        print(row)

    print("\nDisplaying all meals: ")
    for row in cur.execute(SELECT_ALL_MEALS):
        print(row)

    con.close()

if __name__ == "__main__":
    main()
