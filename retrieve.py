# from google.cloud import bigquery
import os

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

app = Flask(house_hunch)

# Define a route to handle incoming data from the frontend
@app.route('/api/upload', methods=['POST'])
def upload_csv():
    file = request.files['csv_file']
    
    if file:
        # Connect to your local SQLite database (you can use other databases as well)
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        
        # Define the table structure in your database
        cursor.execute('''CREATE TABLE IF NOT EXISTS "HomeBuyerInfo" ("ID" INTEGER PRIMARY KEY AUTOINCREMENT, "GrossMonthlyIncome " INTEGER NOT NULL, "CreditCardPayment " INTEGER NOT NULL, "CarPayment " INTEGER NOT NULL, "StudentLoanPayments " INTEGER NOT NULL, "AppraisedValue " INTEGER NOT NULL, "DownPayment " REAL NOT NULL, "LoanAmount " REAL NOT NULL, "MonthlyMortagePayment " REAL NOT NULL, "CreditScore " INTEGER NOT NULL)''')
        
        # Read and import the CSV data into the database
        csv_data = csv.reader(file)
        next(csv_data, None)  # Skip the header row if present
        with open('your_data.csv', 'r') as csv_file:
            csv_data = csv.reader(csv_file)
            next(csv_data, None)  # Skip the header row if present

            for row in csv_data:
                cursor.execute('''INSERT INTO "HomeBuyerInfo" (
                    "Id",
                    "GrossMonthlyIncome",
                    "CreditCardPayment",
                    "CarPayment",
                    "StudentLoanPayments",
                    "AppraisedValue",
                    "DownPayment",
                    "LoanAmount",
                    "MonthlyMortgagePayment",
                    "CreditScore"
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', row)
        
        conn.commit()
        conn.close()
        
        return jsonify({"success": True})
    else:
        return jsonify({"success": False, "error": "No file uploaded"})

if __name__ == '__main__':
    app.run(debug=True)
