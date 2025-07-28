import sqlite3
from database_func import *
from constants import *

def main():
    print("Hello from backend!")
    con = sqlite3.connect("mealprep.db")
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()

    build_tables(con, cur)

    #Even though columns are not required/null-able, we must still provide data for every column when inserting. Any values we do not have will required defaults like null. 
    tables = cur.execute(SELECT_ALL_TABLES)
    print(tables.fetchall())

    insert_sample_data(con, cur)
    insert_todays_sample_meal(con, cur)

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
    print("Displaying all foods rows: ")
    for row in cur.execute(SELECT_ALL_FOODS):
        print(row)

    print("\nDisplaying all meals rows: ")
    for row in cur.execute(SELECT_ALL_MEALS):
        print(row)

    print("\nDisplaying all days rows: ")
    for row in cur.execute(SELECT_ALL_DAYS):
        print(row)

    print()
    data = get_data("foods", cur)
    print(f"Foods Data: {data}")
    data_2 = get_data("meals", cur)
    print(f"Meals Data: {data_2}")
    data_3 = get_data("days", cur)
    print(f"Days Data: {data_3}")
    print()
    print("Meal Macro: ")
    for row in cur.execute(SELECT_MEAL_MACRO):
        print(row)
    print("Testing get meal data:")
    final_form = get_meals_data(cur)
    print(final_form)
    # write_json(data, "foods")
    write_json(final_form, "meals")
    # write_json(data_3, "days")

    con.close()

if __name__ == "__main__":
    main()
