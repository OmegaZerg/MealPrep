from constants import *
from datetime import date
import json

def build_tables(connection, cursor):
        if not table_exists("foods", cursor):
            try:
                cursor.execute(CREATE_FOODS_TABLE)
                connection.commit()
            except Exception as e:
                #TODO: Possibly create a backup database file with the tables and default data in place, and could pull from that if this fails for some reason?
                print(f"ERROR: Unable to create the foods table - {e}\n")    
        if not table_exists("meals", cursor):
            try:
                cursor.execute(CREATE_MEALS_TABLE)
                connection.commit()
            except Exception as e:
                #TODO: Possibly create a backup database file with the tables and default data in place, and could pull from that if this fails for some reason?
                print(f"ERROR: Unable to create the meals table - {e}\n")
        if not table_exists("days", cursor):
            try:
                cursor.execute(CREATE_DAYS_TABLE)
                connection.commit()
            except Exception as e:
                #TODO: Possibly create a backup database file with the tables and default data in place, and could pull from that if this fails for some reason?
                print(f"ERROR: Unable to create the days table - {e}\n")

def table_exists(table_name: str, cursor):
    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' AND name=?;
    """, (table_name,))
    return cursor.fetchone() is not None

def insert_sample_data(connection, cursor):
    try:
        cursor.executemany("INSERT INTO foods VALUES (?, ?, ?, ?, ?, ?, ?, ?)", SAMPLE_FOODS)
        connection.commit()
    except Exception as e:
        print(f"ERROR: Unable to write to the foods table - {e}\n")

    try:
        cursor.executemany("INSERT INTO meals VALUES (?, ?, ?, ?, ?, ?, ?, ?)", SAMPLE_MEALS)
        connection.commit()
    except Exception as e:
        print(f"ERROR: Unable to write to the meals table - {e}\n")

def insert_todays_sample_meal(connection, cursor):
    today = date.today()
    formatted_date = today.strftime("%d-%m-%Y")

    try:
        todays_meal = cursor.execute("SELECT * FROM days WHERE meal_date = ?", [(formatted_date),])
        print(f"Todays Meal: {todays_meal.fetchone()}")
    except Exception as e:
        print(f"ERROR: Unable to select from the days table - {e}")

    if not todays_meal:
        try:
            cursor.executemany("INSERT INTO days VALUES (?, ?, ?, ?)", [(formatted_date, "Breakfast 1", "Lunch 1", "Dinner 1"),])
            connection.commit()
        except Exception as e:
            print(f"ERROR: Unable to write to the days table - {e}\n")

def insert_foods():
    pass

def insert_meals():
    pass

def insert_days():
    pass

def update_foods():
    pass

def update_meals():
    pass

def update_days():
    pass

def get_data(table_name: str, cursor):
    if not table_name:
        print("Table name was not provided and is required to perform read operations")
        return
    match table_name:
        case "foods":
            try:
                data = {}
                for i, row in enumerate(cursor.execute(SELECT_ALL_FOODS)):
                    element = {}
                    for j, column in enumerate(row):
                        #print(f"J: {j}, column: {column}")
                        match j:
                            case 0:
                                element["food_name"] = column
                            case 1:
                                element["description"] = column
                            case 2:
                                element["unit"] = column
                            case 3:
                                element["quantity"] = column
                            case 4:
                                element["calories"] = column
                            case 5:
                                element["fat"] = column
                            case 6:
                                element["carbs"] = column
                            case 7:
                                element["protein"] = column
                            case _:
                                print(f"Unknown column {j}: {column} - issue with retrieving data for foods table.")
                    data[i] = element
            except Exception as e:
                print(f"ERROR: Unable to read from the foods table - {e}\n")
        case "meals":
            try:
                data = {}
                for i, row in enumerate(cursor.execute(SELECT_ALL_MEALS)):
                    element = {}
                    for j, column in enumerate(row):
                        #print(f"J: {j}, column: {column}")
                        match j:
                            case 0:
                                element["meal_name"] = column
                            case 1:
                                element["description"] = column
                            case 2:
                                element["tag"] = column
                            case 3:
                                element["food_1"] = column
                            case 4:
                                element["food_2"] = column
                            case 5:
                                element["food_3"] = column
                            case 6:
                                element["food_4"] = column
                            case 7:
                                element["food_5"] = column
                            case _:
                                print(f"Unknown column {j}: {column} - issue with retrieving data for meals table.")
                    data[i] = element
            except Exception as e:
                print(f"ERROR: Unable to read from the meals table - {e}\n")
        case "days":
            try:
                data = {}
                for i, row in enumerate(cursor.execute(SELECT_ALL_DAYS)):
                    element = {}
                    for j, column in enumerate(row):
                        match j:
                            case 0:
                                element["meal_date"] = column
                            case 1:
                                element["breakfast"] = column
                            case 2:
                                element["lunch"] = column
                            case 3:
                                element["dinner"] = column
                            case _:
                                print(f"Unknown column {j}: {column} - issue with retrieving data for days table.")
                    data[i] = element
            except Exception as e:
                print(f"ERROR: Unable to read from the days table - {e}\n")
        case _:
            print(f"unknown table name {table_name}")
            return
    return data
#TODO: Will require logic to ensure that when adding meals to a slot(like breakfast) that the tag for the meal is 'breakfast'. Possibly do via form validation on front end isntead.
def add_meal_to_day():
    pass

def write_json(data: str, table: str):
    match table:
        case "foods":
            try:
                with open("test_json/foods_indent.json", mode="w", encoding="utf-8") as write_file:
                    json.dump(data, write_file, indent=4)
            except Exception as e:
                print(f"ERROR: Unable to write out the JSON file - {e}")

            try:
                with open("test_json/foods_blob.json", mode="w", encoding="utf-8") as write_file:
                    json.dump(data, write_file)
            except Exception as e:
                print(f"ERROR: Unable to write out the JSON file - {e}")
        case "meals":
            try:
                with open("test_json/meals_indent.json", mode="w", encoding="utf-8") as write_file:
                    json.dump(data, write_file, indent=4)
            except Exception as e:
                print(f"ERROR: Unable to write out the JSON file - {e}")
        case "days":
            try:
                with open("test_json/days_indent.json", mode="w", encoding="utf-8") as write_file:
                    json.dump(data, write_file, indent=4)
            except Exception as e:
                print(f"ERROR: Unable to write out the JSON file - {e}")
        case _:
            print(f"ERROR: Unknown table name entered...")

