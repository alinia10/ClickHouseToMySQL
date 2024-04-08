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
def copy_table_from_mysql_to_clickhouse():
    query = f"CREATE TABLE IF NOT EXISTS {TABLE_} (\
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
    query = f"CREATE TABLE IF NOT EXISTS {DATABASE_}.{NEWTABLE_} (\
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
    ) ENGINE = MergeTree() ORDER BY id;"

    client.execute(query)

    query = f"INSERT INTO {DATABASE_}.{NEWTABLE_} SELECT * FROM {DATABASE_}.{TABLE_};"
    client.execute(query)


query = f'USE {DATABASE_};'


start_time = time.time() * 1000  # Start time in milliseconds
copy_table_from_mysql_to_clickhouse()
end_time = time.time() * 1000  # End time in milliseconds
execution_time_ms = end_time - start_time
print("Insert time:", execution_time_ms, "ms")

query =f"SELECT count(DISTINCT name) FROM {DATABASE_}.{NEWTABLE_} ;"

start_time = time.time() * 1000  # Start time in milliseconds
result = client.execute(query)
end_time = time.time() * 1000  # End time in milliseconds

execution_time_ms = end_time - start_time
print("Execution time:", execution_time_ms, "ms")
# print(result)
