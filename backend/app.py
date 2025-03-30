from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Farmers App Backend'}), 200

@app.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')

    # Sample response logic
    if question:
        return jsonify({'response': f'We received your question: {question}'}), 200
    else:
        return jsonify({'error': 'No question received'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
