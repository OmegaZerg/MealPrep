import sqlite3
from constants import *

def table_exists(table_name: str, cursor):
    cursor.execute("""
        SELECT name 
        FROM sqlite_master 
        WHERE type='table' AND name=?;
    """, (table_name,))
    return cursor.fetchone() is not None

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
            #TODO: Need to implement
            print("Days not implemented yet")
            return
        case _:
            print(f"unknown table name {table_name}")
            return
    return data
#TODO: Will require logic to ensure that when adding meals to a slot(like breakfast) that the tag for the meal is 'breakfast'. Possibly do via form validation on front end isntead.
def add_meal_to_day():
    pass

#TODO: Possibly add function to generate date based on today date for the sample days.