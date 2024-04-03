import pandas as pd
from faker import Faker
import csv

# Initialize Faker
fake = Faker()

# Define the number of rows
num_rows = 2000000  # adjust this number to achieve the desired file size

# Create a list of dictionaries to hold data
data = []

# Generate data
for i in range(num_rows):
    row = {
        'id': str(i).zfill(12),  # Incremental unique 12-digit ID
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'job': fake.job(),
        'company': fake.company(),
        'city': fake.city(),
        'country': fake.country(),
        'date': fake.date(),
    }
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Write DataFrame to CSV
df.to_csv('fake_data.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)

print("CSV file generated successfully.")

