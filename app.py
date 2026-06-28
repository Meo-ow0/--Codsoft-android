from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

# Database set up so app has a place to store task.
# If it's running first time app the required table is created.
database.init_db()


# This is the main page of the application.
# This will load every task from the database and shows them to the user.
@app.route('/')
def index():
    return render_template('index.html', tasks=database.get_tasks())


# Handles the form when a user adds a new task.
# Once submitted, the task is saved and the user is taken back to the task list.
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    deadline = request.form.get('deadline')  # getting deadline from form

    # Ignore empty submissions so blank tasks aren't stored.
    if task:
        database.add_task(task, deadline)

    return redirect('/')


# Removes a task using its unique ID.
# This lets users clear completed or unwanted items from their list.
@app.route('/delete/<int:task_id>')
def delete(task_id):
    database.delete_task(task_id)
    return redirect('/')


# Run the application in development mode.
# Debug mode makes it easier to test changes while building the project.
if __name__ == '__main__':
    app.run(debug=True)