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
    cursor.execute(f"DROP DATABASE IF EXISTS {DATABASE_}")
    print("Database dropped")
    mydb.commit()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_}")
    print("Database created")
    mydb.commit()
# Function to create a table
def create_table():
    cursor.execute(f"USE {DATABASE_}")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_} (\
        `id` INT AUTO_INCREMENT PRIMARY KEY,\
        `name` VARCHAR(255),\
        `address` VARCHAR(255),\
        `email` VARCHAR(255),\
        `phone_number` VARCHAR(30),\
        `job` VARCHAR(255),\
        `company` VARCHAR(255),\
        `city` VARCHAR(255),\
        `country` VARCHAR(255),\
        `date` VARCHAR(255)\
    );")

def insert_data_real_time():
    with open('../mysql_data_directory/fake_data.csv', 'r') as file:
        next(file)  # Skip the first row

        for line in file:
            # print(line)
            line = line.split(',')
            name = line[0]
            address = line[1]
            email = line[2]
            phone_number = line[3]
            job = line[4]
            company = line[5]
            city = line[6]
            country = line[7]
            date = line[8]
            sql = f"INSERT INTO {TABLE_} (name, address, email, phone_number, job, company, city, country, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (name, address, email, phone_number, job, company, city, country, date)
            cursor.execute(sql, val)
            # mydb.commit()
            # print("Inserted:", val)
        mydb.commit()

def insert_data_csv():
    try:
        # Modify the following query according to your table structure and CSV file path
        query = f"""
        LOAD DATA INFILE '/var/lib/mysql-files/fake_data.csv'
        INTO TABLE {TABLE_}
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        IGNORE 1 LINES
        (name, address, email, phone_number, job, company, city, country, date);
        """
        cursor.execute(query)
        mydb.commit()
        print("Data inserted from CSV successfully.")
    except mysql.connector.Error as err:
        print(f"An error occurred: {err}")


# Call the functions to create database and table
# create_database()
# create_table()
# insert_data_csv()
# # Call the main function
# insert_data_real_time()
cursor.execute(f"USE {DATABASE_}")

insert_data_csv()