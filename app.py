from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)
database.init_db()

@app.route('/')
def index():
    return render_template('index.html', alarms=database.get_alarms())

@app.route('/add', methods=['POST'])
def add():
    time = request.form.get('time')
    label = request.form.get('label')
    if time:
        database.add_alarm(time, label)
    return redirect('/')

@app.route('/delete/<int:alarm_id>')
def delete(alarm_id):
    conn = database.get_db()
    conn.execute("DELETE FROM alarms WHERE id = ?", (alarm_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)