import os
dir_path = "/"
file_name = "coconut.jpg"
found = False
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file == file_name:
            found = True
            break
if found:
    print("The file was found.")
else:
    print("The file was not found.")
