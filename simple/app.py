from flask import Flask, jsonify, render_template, request
from datetime import datetime 
app = Flask(__name__) 

@app.route('/home')
def home():
    current_day = datetime.now().strftime('%A')
    topics = "devops, it assets, inventory, management"
    return render_template('home.html', current_day=current_day, topics=topics)

if __name__ == '__main__':
    app.run(debug=True)