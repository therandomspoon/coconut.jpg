import requests
import os
import time
dir_path = input("Enter the directory path to save the file: ")
if not os.path.isdir(dir_path):
    print(f"The directory {dir_path} does not exist.")
    exit()
url = "https://raw.githubusercontent.com/therandomspoon/coconut.jpg/main/coconut.jpg"
response = requests.get(url)
if response.status_code == 200:
    file_name = os.path.basename(url)
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"The file {file_name} has been downloaded and saved to {file_path}.")
    time.sleep(100)
else:
    print(f"Failed to download the file from {url}. Status code: {response.status_code}")
    time.sleep(100)
