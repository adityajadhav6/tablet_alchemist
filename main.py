import sys
import os
from flask import Flask
from src.routes import routes  # Import the Blueprint

# Ensure src folder is accessible
sys.path.append(os.path.abspath("src"))

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True)
