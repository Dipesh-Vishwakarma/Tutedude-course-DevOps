import os
import json
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the GET /api route
@app.route("/api", methods=["GET"])
def get_data():
    """
    Route handler for /api.
    Reads data from backend/data.json and returns it as a JSON response.
    Includes basic error handling for file not found and invalid JSON format.
    """
    # Construct absolute path to backend/data.json based on app root path
    file_path = os.path.join(app.root_path, "backend", "data.json")

    # Error Handling Step 1: Check if data.json file exists
    if not os.path.exists(file_path):
        return jsonify({"error": "Data file not found"}), 404

    try:
        # Step 2: Open and read the JSON file using Python's built-in json module
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Step 3: Return the parsed data as a JSON response with status code 200 (OK)
        return jsonify(data), 200

    except json.JSONDecodeError:
        # Error Handling Step 2: Handle invalid JSON formatting in backend/data.json
        return jsonify({"error": "Invalid JSON format in data file"}), 500

    except Exception as e:
        # Error Handling Step 3: Catch any other unexpected server errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask application in debug mode on port 5000 when executed directly
if __name__ == "__main__":
    app.run(debug=True, port=5000)
