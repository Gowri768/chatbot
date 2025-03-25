from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# Configure API key (Replace with your actual API key)
GOOGLE_API_KEY = "AIzaSyDpZgmcroy2U2lmusR7hnhtMWi3Sg5rJiM"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Generative AI Model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)
CORS(app)  # Enable CORS to prevent frontend issues

@app.route('/')
def index():
    return render_template('index1.html')  # Ensure 'index1.html' is inside 'templates' folder

@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response_raw = chat.send_message(user_input)
        response = response_raw.text  # Extract text response
        return jsonify({"response": response})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
