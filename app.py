from flask import Flask, render_template, request, jsonify
import csv
import os
import subprocess
import datetime

app = Flask(__name__)

# Get the username of the currently logged in user
global_username = None
LOG_FILE = 'login_attempts.log'



ip_add = { 'table_A': '1.1.1.1',
            'table_B': '2.2.2.2'
            }


# Greeting Function 
def get_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good Morning"
    else:
        return "Good Afternoon"

# Function to read CSV file and return data as a list of dictionaries
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form['username']
    return redirect(url_for('index'))


# Function to set the global username
def set_global_username(username):
    global global_username
    global_username = username
    print(f"Global username set to: {global_username}")

# Function to get the global username
def get_global_username():
    return global_username

@app.route('/')
def index():
    # Read log data
    log_data = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as file:
            for line in file:
                log_data.append(line.strip().split(','))

    # Reverse the log data to show the latest attempts first
    log_data.reverse()
    log_data_with_index = [[i+1] + log for i, log in enumerate(log_data)]

    username = os.getlogin()
    greeting = get_greeting()  # Get the greeting based on the current time
    return render_template('index.html', username=global_username, active_page='home', log_data=log_data_with_index, greeting=greeting)
    # return render_template('index.html', data=data, username=USERNAME, active_page='home', log_data=log_data)

@app.route('/set_username', methods=['POST'])
def set_username():
    data = request.get_json()
    username = data.get('username')
    if username:
        set_global_username(username)
        return jsonify(success=True), 200
    else:
        return jsonify(success=False), 400

# Function to record loggig attempts.
@app.route('/log_attempt', methods=['POST'])
def log_attempt():
    # Extract data from the request
    # username = USERNAME
    username = os.getlogin()
    user_ip = request.remote_addr
    putty_ip = request.form['putty_ip']
    port = request.form['port']
    status = request.form['status']
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log the attempt
    with open(LOG_FILE, 'a') as file:
        file.write(f"{timestamp},{username},{user_ip},{putty_ip},{port},{status}\n")

    return 'Logged'

# Route for Table A
@app.route('/table_a')
def table_a():
    data = read_csv('db/table_a.csv')
    return render_template('table.html', data=data, table='A', ip = '1.1.1.1', username=global_username, active_page='table_a')


# Route for Table B
@app.route('/table_b')
def table_b():
    data = read_csv('db/table_b.csv')
    return render_template('table.html', data=data, table='B', ip= 'bandit.labs.overthewire.org', username=global_username, active_page='table_b')


if __name__ == '__main__':
    app.run(debug=True)
