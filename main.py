import sys
import os
from flask import Flask, request, render_template, jsonify

# Ensure src folder is accessible
sys.path.append(os.path.abspath("src"))

from alchemist import get_tablet_details, get_recommendations, search_tablets

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["GET"])
def recommend():
    condition = request.args.get("condition", "").strip().lower()
    age = request.args.get("age", "").strip()
    
    try:
        age = int(age)
    except ValueError:
        age = None  # Handle cases where age is missing or invalid

    tablets = get_recommendations(condition, age)

    return render_template("details.html", condition=condition, tablets=tablets)

@app.route("/tablet/<condition>/<tablet>")
def tablet(condition, tablet):
    tablet_details = get_tablet_details(condition, tablet)
    return render_template("details.html", condition=condition, selected_tablet=tablet_details)

@app.route("/search_tablet", methods=["GET"])
def search_tablet():
    query = request.args.get("query", "").lower()
    results = search_tablets(query)
    return render_template("search_results.html", tablets=results)

@app.route("/autocomplete/conditions")
def autocomplete_conditions():
    """Returns a list of conditions matching the query."""
    query = request.args.get("q", "").lower()
    with open("data/drug_database.json", "r") as f:
        import json
        data = json.load(f)
        conditions = [condition for condition in data.keys() if query in condition]
    return jsonify(conditions)

if __name__ == "__main__":
    app.run(debug=True)
