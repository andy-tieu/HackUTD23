from google.cloud import bigquery
import os

client = bigquery.Client()
query = '''
SELECT *
FROM your_dataset.your_table
WHERE column1 = 'some_value'
'''

query_job = client.query(query)
results = query_job.result()

for row in results:
    print(row)