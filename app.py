from flask import Flask, render_template, request, jsonify
import sqlite3

conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/submit', methods=['POST'])
def submit_data():
    # Handle user input logic here and respond with JSON data
    data = request.get_json()
    # Process data and return a response

# @app.route('/api/get_data', methods=['GET'])
# def get_data():
#     # Execute an SQL query to retrieve data from the database
#     cursor.execute('SELECT * FROM your_table_name')
#     data = cursor.fetchall()
#     column_names = [description[0] for description in cursor.description]

#     # Convert data to a list of dictionaries for JSON serialization
#     data_list = [dict(zip(column_names, row)) for row in data]

#     return jsonify(data_list)


if __name__ == '__main__':
    app.run(debug=True)
