import sys
import os
import json
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
    """Fetches medicine recommendations based on condition and optional age."""
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
    """Displays details of a specific tablet based on condition and name."""
    tablet_details = get_tablet_details(condition, tablet)
    return render_template("details.html", condition=condition, selected_tablet=tablet_details)

@app.route("/search_tablet", methods=["GET"])
def search_tablet():
    """Searches for tablets by name and displays results."""
    query = request.args.get("query", "").strip().lower()
    results = search_tablets(query)
    return render_template("search_results.html", query=query, results=results)

@app.route("/autocomplete/conditions")
def autocomplete_conditions():
    """Returns a list of conditions matching the query for autocomplete."""
    query = request.args.get("q", "").lower()
    
    with open("data/drug_database.json", "r") as f:
        data = json.load(f)
        conditions = [condition for condition in data.keys() if query in condition]

    return jsonify(conditions)

@app.route("/autocomplete/tablets")
def autocomplete_tablets():
    """Returns a list of tablets matching the query for autocomplete."""
    query = request.args.get("q", "").lower()

    with open("data/drug_database.json", "r") as f:
        data = json.load(f)
        tablets = set()
        for meds in data.values():
            for med in meds:
                if query in med["name"].lower():
                    tablets.add(med["name"])

    return jsonify(list(tablets))

if __name__ == "__main__":
    app.run(debug=True)
