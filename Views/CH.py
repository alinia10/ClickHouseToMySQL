from clickhouse_driver import Client
import time
from conf import *

client = Client(
    host=ClickHouse_ip,
    port=9000,
)
print('Connected to ClickHouse')


def create_database():
    query = f"DROP DATABASE IF EXISTS {DATABASE_};"
    client.execute(query)
    query = f"CREATE DATABASE IF NOT EXISTS {DATABASE_};"
    client.execute(query)
    query = f'USE {DATABASE_};'
    client.execute(query)    



create_database()
query = f"CREATE TABLE IF NOT EXISTS {DATABASE_}.{TABLE_} (\
    id UInt32,\
    name String,\
    address String,\
    email String,\
    phone_number String,\
    job String,\
    company String,\
    city String,\
    country String,\
    date String\
) ENGINE = MySQL('{MySQL_ip}:3306', '{DATABASE_}', '{TABLE_}', 'root', '1381');"

client.execute(query)
query =f"SELECT count(DISTINCT name) FROM {DATABASE_}.{TABLE_} ;"

start_time = time.time() * 1000  # Start time in milliseconds
result = client.execute(query)
end_time = time.time() * 1000  # End time in milliseconds

execution_time_ms = end_time - start_time
print("Execution time:", execution_time_ms, "ms")
# print(result)
