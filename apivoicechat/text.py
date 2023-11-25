from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    # user_message = request.form.get('user_message')
    data = request.json
    user_message = data.get('user_message')
    if user_message:
        response = process_user_message(user_message)
    else:
        response = "Invalid input."

    return jsonify({"message": response})
def process_user_message(user_message):
    # Step 1: send the conversation and available functions to GPT
    # Check for greetings
    if user_message.lower() in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today?"
    
if __name__ == '__main__':
    app.run(debug=True)
