import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/drug_database.json")

def load_database():
    """Loads the drug database from a JSON file."""
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database file not found: {DB_PATH}")

    with open(DB_PATH, "r") as f:
        return json.load(f)

def is_age_suitable(age_range, user_age):
    """Checks if the medicine is suitable for the given age."""
    if not age_range or age_range == "all":
        return True
    try:
        min_age, max_age = map(int, age_range.split('-'))
        return min_age <= user_age <= max_age
    except ValueError:
        return True  # Fallback if age_range is incorrectly formatted

def get_recommendations(condition, age=None):
    """Returns a list of recommended tablets for a condition and age."""
    data = load_database()
    if condition not in data:
        return []
    
    recommendations = data[condition]
    
    if age is not None:
        recommendations = [med for med in recommendations if is_age_suitable(med.get("age_range", ""), age)]
    
    return recommendations

def get_tablet_details(condition, tablet_name):
    """Returns the details of a specific tablet."""
    data = load_database()
    if condition in data:
        for med in data[condition]:
            if med["name"].lower() == tablet_name.lower():
                return med
    return None

def search_tablets(query):
    """Searches for tablets across all conditions."""
    data = load_database()
    results = []
    for condition, tablets in data.items():
        for tablet in tablets:
            if query.lower() in tablet["name"].lower():
                results.append(tablet)
    return results
