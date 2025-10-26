from flask import Flask, jsonify, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask App!")

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/deshboard', methods=['POST'])
def deshboard():
    return "Welcome to the Dashboard! Mr {username}"
if __name__ == '__main__':
    app.run(debug=True)