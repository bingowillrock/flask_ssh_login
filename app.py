from flask import Flask, render_template, request
import csv
import os
import subprocess

app = Flask(__name__)

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
    username = os.getlogin()  # Get the username of the currently logged in user
    return render_template('index.html', username=username)

# Route for Table A
@app.route('/table_a')
def table_a():
    data = read_csv('table_a.csv')
    return render_template('table.html', data=data, table='A')

# Route for Table B
@app.route('/table_b')
def table_b():
    data = read_csv('table_b.csv')
    return render_template('table.html', data=data, table='B')

@app.route('/ssh')
def ssh():
    router_name = request.args.get('router_name')
    port_number = request.args.get('port_number')
    # Assuming the SSH command is in the format: ssh <router_name> -p <port_number>
    ssh_command = f'ssh {router_name} -p {port_number}'
    subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', ssh_command])
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
