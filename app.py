from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/receive-data', methods=['POST'])
def receive_data():
    data = request.json.get('data')
    print("Received data:", data)
    # Process the received data here
    return 'Data received successfully'

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
