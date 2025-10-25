from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return 'Welcome!'

@app.route('/user/<username>')
def profile(username):
    return f"hello {username}!. this is your profile page."
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"displaying post name:{}"