from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/push_data', methods=['POST'])
def push_data():
    data = request.json

    # Use the data with Ollama (assume you have a function to process data with Ollama)
    processed_data = process_with_ollama(data)

    return jsonify({"status": "success", "processed_data": processed_data})

def process_with_ollama(data):
    # Placeholder for the actual Ollama processing logic
    # You can integrate Ollama's API or any logic you need here
    return data  # Replace with actual processing

if __name__ == '__main__':
    app.run(debug=True, port=5000)
