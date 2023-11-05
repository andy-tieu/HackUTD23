from flask import Flask, render_template, request, jsonify
import sqlite3
import csv
app = Flask(__name__, template_folder='.', static_url_path='')

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    try:
        data = request.get_json()
        
        # Validate the incoming JSON data (optional)
        required_fields = [
            'creditScore', 'grossMonthlyIncome', 'houseValue',
            'downPayment', 'mortgage', 'creditCardPayment',
            'carPayment', 'studentLoanPayment'
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing {field} in the JSON data'}), 400

        # Connect to the SQLite database (create it if it doesn't exist)
        conn = sqlite3.connect('mortgage_data.db')
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mortgage_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                creditScore INTEGER,
                grossMonthlyIncome REAL,
                houseValue REAL,
                downPayment REAL,
                mortgage REAL,
                creditCardPayment REAL,
                carPayment REAL,
                studentLoanPayment REAL
            )
        ''')

        # Insert the JSON data into the database
        cursor.execute('''
            INSERT INTO mortgage_data (
                creditScore, grossMonthlyIncome, houseValue,
                downPayment, mortgage, creditCardPayment,
                carPayment, studentLoanPayment
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['creditScore'], data['grossMonthlyIncome'],
            data['houseValue'], data['downPayment'],
            data['mortgage'], data['creditCardPayment'],
            data['carPayment'], data['studentLoanPayment']
        ))

        # Commit the changes and close the database connection
        conn.commit()
        conn.close()

        return jsonify({'message': 'Data successfully added to the database'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
    app.run(port=5000)  # Modify 'app' and set the desired port