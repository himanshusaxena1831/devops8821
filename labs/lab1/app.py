from flask import Flask, render_template
app = Flask(__name__) 

# @app.route('/')
# def show_todos():
#     my_todos = [ 
#         "finish flask tutorial",
#         "grocery shopping",
#         "read a chapter of a book",
#         "go for walk "
#     ]
#     return render_template('todos.html', todos_item=my_todos, page_title="My To-Do List")
@app.route('/todos')
def show_todos():
    my_todos = [
        "Finish Flask tutorial",
        "Grocery shopping",
        "Read a chapter of a book",
        "Go for a walk"
    ]
    # To test the 'else' case in Jinja, you can temporarily set:
    # my_todos = [] 
    return render_template('todos.html', todo_items=my_todos, page_title="My To-Do List")
if __name__ == '__main__':
    app.run(debug=True)