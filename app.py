from flask import Flask, render_template, request
import csv
import os
import subprocess

app = Flask(__name__)

# Get the username of the currently logged in user
USERNAME = os.getlogin()

# Function to read CSV file and return data as a list of dictionaries
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', username=USERNAME, active_page='home')

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

@app.route('/ssh')
def ssh():
    router_name = request.args.get('router_name')
    port_number = request.args.get('port_number')
    # Assuming the SSH command is in the format: ssh <router_name> -p <port_number>
    ssh_command = f'ssh {router_name} -p {port_number}'
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', ssh_command])
    return '', 204

# Route for initiating SSH session
@app.route('/initiate_ssh', methods=['POST'])
def initiate_ssh():
    ip_address = request.form['ip_address']
    port_number = request.form['port_number']
    # You can customize this command as per your requirements
    command = f"powershell Start-Process ssh -ArgumentList 'username@{ip_address} -p {port_number}'"
    subprocess.Popen(command, shell=True)
    return 'SSH session initiated successfully'

if __name__ == '__main__':
    app.run(debug=True)
