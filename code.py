
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, helpful for development

@app.route('/')
def hello_world():
    return jsonify(message='Hello from Flask API!')

@app.route('/api/sample', methods=['GET'])
def get_sample_data():
    """
    A sample API endpoint that returns JSON data.
    """
    data = {
        "id": 1,
        "name": "Sample Item",
        "description": "This is a sample item from the Flask API.",
        "version": "1.0.0"
    }
    return jsonify(data)


@app.route('/api/process', methods=['POST'])
def process_data():
    """
    A sample API endpoint to demonstrate receiving POST data.
    This is a placeholder and would need actual data handling.
    """
    # from flask import request
    # if request.is_json:
    #     content = request.get_json()
    #     # Process content here
    #     return jsonify({"status": "success", "received_data": content}), 200
    # else:
    #     return jsonify({"status": "error", "message": "Request must be JSON"}), 400
    return jsonify({"status": "placeholder", "message": "This endpoint is ready to process POST data."})


if __name__ == '__main__':
   
    app.run(debug=True, port=5001) # Ensure this port is different from your Next.js app
