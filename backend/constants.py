SAMPLE_FOODS = [
    ("Scrambled Eggs", "Whole eggs with yolk", "Ounce", 4, 169, 13, 2, 12),
    ("Toast", "1 Piece with butter", "Slice", 1, 180, 9, 21, 4),
    ("Milk", "1 cup of milk", "Ounce", 8, 100, 3, 8, 9),
    ("Turkey Sandwhich", "2 bread, 4 ounces turkey lunchmeat, lettuce, tomato, onion, mustard", None, 1, 360, 7, 40, 36),
    ("Spinach Salad", "Large salad with light italian dressing", None, 1, 140, 5, 21, 5),
    ("Honeycrisp Apple", "Its an apple", "Ounce", 8, 118, 0, 32, 0),
    ("Orange Juice", "1 cup of orange juice", "Ounch", 8, 117, 1, 25, 2),
    ("Banana", "Its a banana", None, 1, 114, 0, 27, 1),
    ("Plain Oatmeal", "Plain old quaker oats, cooked", "Ounce", 7, 136, 2, 24, 5),
    ("Pure Protein Protein Bar", "Its packed full of flavores and proteins. Deluxe Chocolate.", None, 1, 180, 5, 17, 21),
    ("NY Strip Steak", "Cooked beef ultra premium first cut prime established - grilled (of course)", "Ounce", 7, 310, 12, 0, 46),
    ("Cliff Bar - Chocolate Chip", "Energy Bar that helps you climb mountains..or something", None, 1, 250, 6, 43, 10),
    ("Progresso Chickpea and Noodle Soup", "18.5 ounce can of soup", None, 1, 340, 7, 53, 17),
    ("Collard Greens", "Steamed greens", "gram", 100, 29, 1, 6, 4),
    ("Red Potato", "Plain with salf/pepper", "Ounce", 5, 138, 0, 33, 4),
]
SAMPLE_MEALS = [
    ("Lunch 1", "Sandwhich, apple, and salad", "Lunch", "Turkey Sandwhich", "Honeycrisp Apple", "Spinach Salad", None, None),
    ("Breakfast 1", "Toast, scrambled eggs, and orange juice", "Breakfast", "Scrambled Eggs", "Toast", "Orange Juice", None, None),
    ("Dinner 1", "Steak, greens, and potatoes", "Dinner", "NY Strip Steak", "Collard Greens", "Red Potato", None, None),
]
SAMPLE_DAYS = [
    ("28-07-2025", "Breakfast 1", "Lunch 1", "Dinner 1"),
]
CREATE_FOODS_TABLE = """
CREATE TABLE foods (
    food_name TEXT PRIMARY KEY NOT NULL,
    description TEXT NULL,
    unit TEXT NULL,
    quantity INTEGER NULL,
    calories INTEGER NULL,
    fat INTEGER NULL,
    carbs INTEGER NULL,
    protein INTEGER NULL
);
"""
CREATE_MEALS_TABLE = """
CREATE TABLE meals (
    meal_name TEXT PRIMARY KEY NOT NULL,
    description TEXT NULL,
    tag TEXT NOT NULL,
    food_1 TEXT NOT NULL,
    food_2 TEXT NULL,
    food_3 TEXT NULL,
    food_4 TEXT NULL,
    food_5 TEXT NULL,
    FOREIGN KEY (food_1) REFERENCES foods (food_name),
    FOREIGN KEY (food_2) REFERENCES foods (food_name),
    FOREIGN KEY (food_3) REFERENCES foods (food_name),
    FOREIGN KEY (food_4) REFERENCES foods (food_name),
    FOREIGN KEY (food_5) REFERENCES foods (food_name)
);
"""
CREATE_DAYS_TABLE = """
CREATE TABLE days (
    meal_date TEXT NOT NULL,
    breakfast TEXT NOT NULL,
    lunch TEXT NOT NULL,
    dinner TEXT NOT NULL,
    FOREIGN KEY (breakfast) REFERENCES meals (meal_name),
    FOREIGN KEY (lunch) REFERENCES meals (meal_name),
    FOREIGN KEY (dinner) REFERENCES meals (meal_name)
);
"""
SELECT_ALL_TABLES = """
SELECT * FROM sqlite_master;
"""

SELECT_ALL_FOODS = """
SELECT * FROM foods
ORDER BY food_name ASC;
"""

SELECT_ALL_MEALS = """
SELECT * FROM meals
ORDER BY meal_name ASC;
"""

SELECT_ALL_DAYS = """
SELECT * FROM days
ORDER BY meal_date DESC;
"""