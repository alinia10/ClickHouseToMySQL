from clickhouse_driver import Client
import time
from conf import *

client = Client(
    host=ClickHouse_ip,
    port=9000,
)
print('Connected to ClickHouse')
query = f"DROP DATABASE IF EXISTS {DATABASE_};"
client.execute(query)
query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_};"
client.execute(query)

# Drop the table if it exists
query = f"DROP TABLE IF EXISTS {DATABASE_}.{TABLE_};"
client.execute(query)

query = f"CREATE TABLE IF NOT EXISTS {DATABASE_} (\
    id UInt32 DEFAULT generateUUIDv4(),\
    name String,\
    age UInt8,\
    email String) \
    ENGINE = MySQL('{MySQL_ip}:3306', '{DATABASE_}', '{TABLE_}', 'root', '1381');"
client.execute(query)
query = f"SELECT age FROM {DATABASE_} ORDER BY age LIMIT 100;"

start_time = time.time() * 1000  # Start time in milliseconds
result = client.execute(query)
end_time = time.time() * 1000  # End time in milliseconds

execution_time_ms = end_time - start_time
print("Execution time:", execution_time_ms, "ms")
# print(result)
