from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Mr. Brain is active", "status": "online"})

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    user_message = user_data.get("message", "")
    
    # Hapa ndipo unaweza kuweka akili ya AI yako baadaye
    # Kwa sasa, tunamfanya ajibu kitu rahisi
    bot_response = f"Nimepokea ujumbe wako: '{user_message}'. Mimi ni Mr. Brain, niko tayari kukusaidia!"
    
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)

