import sqlite3
from database_func import *
from constants import *

def main():
    print("Hello from backend!")
    con = sqlite3.connect("mealprep.db")
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    if not table_exists("foods", cur):
        try:
            cur.execute(CREATE_FOODS_TABLE)
            con.commit()
        except Exception as e:
            #TODO: Possibly create a backup database file with the tables and default data in place, and could pull from that if this fails for some reason?
            print(f"ERROR: Unable to create the foods table - {e}\n")    
    if not table_exists("meals", cur):
        try:
            cur.execute(CREATE_MEALS_TABLE)
            con.commit()
        except Exception as e:
            #TODO: Possibly create a backup database file with the tables and default data in place, and could pull from that if this fails for some reason?
            print(f"ERROR: Unable to create the meals table - {e}\n")

    #Even though columns are not required/null-able, we must still provide data for every column when inserting. Any values we do not have will required defaults like null. 
    tables = cur.execute(SELECT_ALL_TABLES)
    print(tables.fetchall())

    #Testing foods
    try:
        cur.executemany("INSERT INTO foods VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", SAMPLE_FOODS)
        con.commit()
    except Exception as e:
        print(f"ERROR: Unable to write to the foods table - {e}\n")

    #Testing meals
    try:
        cur.executemany("INSERT INTO meals VALUES (?, ?, ?, ?, ?, ?, ?, ?)", SAMPLE_MEALS)
        con.commit()
    except Exception as e:
        print(f"ERROR: Unable to write to the meals table - {e}\n")

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
