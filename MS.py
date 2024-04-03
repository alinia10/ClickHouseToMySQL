import mysql.connector
import time
from conf import *



# Connect to the MySQL server
mydb = mysql.connector.connect(
    host=MySQL_ip,
    user="root",
    password="1381",
    database=DATABASE_
)

cursor = mydb.cursor()



# Query execution with time measurement
start_time = time.time()
query =f"SELECT * FROM {TABLE_} ORDER BY name LIMIT 100;"
cursor.execute(query)
end_time = time.time()

# Fetching results
result = cursor.fetchone()
print("Number of records:", result[0])
# Calculating and printing the time taken in milliseconds
query_time_ms = (end_time - start_time) * 1000
print("Time taken for the query:", query_time_ms, "milliseconds")

# cursor.close()
# mydb.close()