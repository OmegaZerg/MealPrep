SAMPLE_FOODS = [
    ("Scrambled Eggs", "Whole eggs with yolk", "Ounce", 4, 169, 13, 2, 12, "N/A"),
    ("Toast", "1 Piece with butter", "Slice", 1, 180, 9, 21, 4, "N/A"),
    ("Milk", "1 cup of milk", "Ounce", 8, 100, 3, 8, 9, "N/A"),
]
CREATE_FOODS_TABLE = """
CREATE TABLE foods (
    food_name TEXT PRIMARY KEY NOT NULL,
    description TEXT NULL,
    unit TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    calories INTEGER NULL,
    fat INTEGER NULL,
    carbs INTEGER NULL,
    protein INTEGER NULL,
    tag TEXT NULL
);
"""
SELECT_ALL_TABLES = """
SELECT * FROM sqlite_master;
"""

SELECT_ALL_FOODS = """
SELECT * FROM foods
ORDER BY food_name DESC;
"""