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

# from flask import Flask, request, jsonify
import sqlite3
import csv

# app = Flask(house_hunch)

# Define a route to handle incoming data from the frontend
# @app.route('/api/upload', methods=['POST'])
def upload_csv():

    with open('C:\\Users\\fawaz\\OneDrive\\Documents\\GitHub\\HackUTD23\\HackUTD-2023-HomeBuyerInfo.csv','r') as f:
        readfile = csv.reader(f)

        connDB = sqlite3.connect('C:\\Users\\fawaz\\OneDrive\\Documents\\GitHub\\HackUTD23\\HouseHunch.db')
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
    upload_csv()
