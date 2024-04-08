DATABASE_ = "testMerge_db"
TABLE_ = "users"
MySQL_ip = "172.28.0.2"
ClickHouse_ip = "172.28.0.3"
NEWTABLE_ = "users2"
import os
import requests

def download_file(url, save_path):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Write the content to the file
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully at {save_path}")
    else:
        print("Failed to download the file.")

def Download_data():
    # URL of the file to download
    url = "https://iutbox.iut.ac.ir/index.php/s/8TyzoCEQbaMsaTH/download/fake_data.csv"
    
    # Directory to save the file
    directory = "../mysql_data_directory"
    
    # File name
    filename = "fake_data.csv"
    
    # Full path to the file
    file_path = os.path.join(directory, filename)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        # If the file does not exist, download it
        download_file(url, file_path)
    else:
        print("File already exists.")