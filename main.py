import os
import time
dir_path = "/"
file_name = "coconut.jpg"
filecounter = 0
found = False
for root, dirs, files in os.walk(dir_path):
    for file in files:
        filecounter =filecounter + 1
        print(file)
        if file == file_name:
            found = True
            break
if found:
    print("The file was found.")
    print("files counted", filecounter)
    time.sleep(1000)
else:
    print("The file was not found.")
    time.sleep(1000)
