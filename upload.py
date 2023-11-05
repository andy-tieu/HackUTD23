# from google.cloud import bigquery

# import os

# client = bigquery.Client()
# query = '''
# SELECT *
# FROM your_dataset.your_table
# WHERE column1 = 'some_value'
# '''

# query_job = client.query(query)
# results = query_job.result()

# for row in results:
#     print(row)

from flask import Flask, request, jsonify
import sqlite3
import csv

app = Flask(__name__)

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

# Define a route to handle incoming data from the frontend
# @app.route('/api/upload', methods=['POST'])
def upload_csv():

    with open('./HackUTD-2023-HomeBuyerInfo.csv','r') as f:
        readfile = csv.reader(f)

        connDB = sqlite3.connect('./HouseHunch.db')
        connectDB = connDB.cursor()
        connectDB.execute('''CREATE TABLE HomeBuyerInfo ("ID" INTEGER PRIMARY KEY AUTOINCREMENT, "GrossMonthlyIncome" DECIMAL NOT NULL, "CreditCardPayment " DECIMAL NOT NULL, "CarPayment " DECIMAL NOT NULL, "StudentLoanPayments " DECIMAL NOT NULL, "AppraisedValue " DECIMAL NOT NULL, "DownPayment " DECIMAL NOT NULL, "LoanAmount " DECIMAL NOT NULL, "MonthlyMortagePayment " DECIMAL NOT NULL, "CreditScore " INTEGER NOT NULL)''')

        for row in readfile:
            connectDB.execute('''INSERT INTO "HomeBuyerInfo" VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
            
        connDB.commit()
        connDB.close()
        
    #     return jsonify({"success": True})
    # else:
    #     return jsonify({"success": False, "error": "No file uploaded"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Modify 'app' and set the desired port