from flask import Flask, render_template, request
import csv
import os
import subprocess
import datetime

app = Flask(__name__)

# Get the username of the currently logged in user
USERNAME = os.getlogin()
LOG_FILE = 'login_attempts.log'

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

# Route for the home page
# @app.route('/')
# def index():
#     return render_template('index.html', username=USERNAME, active_page='home')

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
    return render_template('index.html', username=USERNAME, active_page='home', log_data=log_data_with_index, greeting=greeting)
    # return render_template('index.html', data=data, username=USERNAME, active_page='home', log_data=log_data)


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
    data = read_csv('table_a.csv')
    return render_template('table.html', data=data, table='A', username=USERNAME, active_page='table_a')

# Route for Table B
@app.route('/table_b')
def table_b():
    data = read_csv('table_b.csv')
    return render_template('table.html', data=data, table='B', username=USERNAME, active_page='table_b')

# Route for initiating SSH session
# @app.route('/initiate_ssh', methods=['POST'])
# def initiate_ssh():
#     ip_address = request.form['ip_address']
#     port_number = request.form['port_number']
#     # You can customize this command as per your requirements
#     command = f"powershell Start-Process ssh -ArgumentList 'username@{ip_address} -p {port_number}'"
#     subprocess.Popen(command, shell=True)
#     return 'SSH session initiated successfully'

if __name__ == '__main__':
    app.run(debug=True)
