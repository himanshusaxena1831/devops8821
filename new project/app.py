from flask import Flask, render_template, session, redirect, url_for, request
import os
app = Flask(__name__)
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/dashboard')
def deshboard():
    return render_template('dashboard.html')
@app.route('/add_item')
def add_item():
    return render_template('add_item.html')
@app.route('/view_inventory')
def view_inventory():
    return render_template('view_inventory.html')

    

if __name__ == '__main__':
    app.run(debug=True)
