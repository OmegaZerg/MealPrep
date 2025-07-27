from flask import Flask, request, jsonify
import sqlite3
from database_func import *
from constants import *

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get-meals")
def get_meals():
    con = sqlite3.connect("mealprep.db")
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()
    api_stuff = get_meals_data(cur)
    print(api_stuff)

if __name__ == "__main__":
    app.run(debug=True)