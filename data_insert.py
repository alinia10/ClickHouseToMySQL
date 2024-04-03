import mysql.connector
from faker import Faker
import random
import time
from conf import *

# Connect to the MySQL server
mydb = mysql.connector.connect(
    host=MySQL_ip,
    user="root",
    password="1381",
    database=""
)

# Create a cursor object to execute SQL queries
cursor = mydb.cursor()

# Function to create a database
def create_database():
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_}")

# Function to create a table
def create_table():
    cursor.execute(f"USE {DATABASE_}")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, email VARCHAR(255))")

# Function to generate random data
def generate_random_data():
    fake = Faker()
    name = fake.name()
    age = random.randint(18, 80)
    email = fake.email()
    return name, age, email

# Main function to insert data into MySQL database in real-time
def insert_data_real_time():
    for _ in range (1000_000):
        print(_)
        name, age, email = generate_random_data()
        sql = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"
        val = (name, age, email)
        cursor.execute(sql, val)
        mydb.commit()
        # print("Inserted:", val)
        time.sleep(0.01)  # Adjust the sleep time as per your requirement

# Call the functions to create database and table
create_database()
create_table()

# Call the main function
insert_data_real_time()
