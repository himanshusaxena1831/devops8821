from flask import Flask, request, render_template 
app = Flask(__name__)

@app.route('/')
def submit():
    return render_template('submit.html')

@app.route('/submit')
def handle_submit():
    name = request.args.get('user_name')
    return f'Hello, {name}!'
    if name:
        return f'Hello, {name}!'
    else:
        return 'please enter your name in the form.'
@app.route('/message', methods=['POST'])
def message_from_submit():
    sender = request.form.get('sender_name')
    message = request.form.get('message_text')

    if sender and message:
        print(f"Message from {sender}: {message}")
        return f"Thank you, {sender}, {message} for your message!"
    else:
        return "Please provide both your name and a message."
    
# def handle_message_post():
#     # 'sender_name' and 'message_text' match the 'name' attributes in the HTML form
#     sender = request.form.get('sender_name')
#     message = request.form.get('message_text')

#     if sender and message:
#         # In a real app, you might save this to a database or send an email
#         print(f"Received message via POST from {sender}: {message}") # Prints to server console
#         return f"<h1>Thank you, {sender}, for your message:</h1><p>'{message}'</p><p>(Submitted via POST)</p>"
#     else:
#         return "<h1>Error: Name and message are required.</h1>"    
if __name__ == '__main__':
    app.run(debug=True)