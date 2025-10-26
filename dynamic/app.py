from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/welcome/<user_name>')
def welcome_user(user_name):
    currect_date = datetime.now().strftime("%B %d, %y")
    return render_template('welcome.html', name=user_name, currect_date=currect_date)
if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template
# from datetime import datetime

# app = Flask(__name__)

# @app.route('/welcome/<user_name>')
# def welcome_user(user_name):
#     today_date = datetime.today().strftime("%B %d, %Y") # e.g., May 20, 2024
#     return render_template('welcome.html', name=user_name, current_date=today_date)

# if __name__ == '__main__':
#     app.run(debug=True)
