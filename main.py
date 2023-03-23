import os
import time
dir_path = "/"
file_name = "coconut.jpg"
filecounter = 0
found = False
file_directory = ""
for root, dirs, files in os.walk(dir_path):
    for file in files:
        filecounter += 1
        print(file)
        if file == file_name:
            found = True
            file_directory = root
            break
    if found:
        break
if found:
    print(f"The file '{file_name}' was found in directory '{file_directory}'.")
    print(f"Total files counted: {filecounter}")
    time.sleep(1000)
else:
    print("The file was not found.")
    time.sleep(1000)
