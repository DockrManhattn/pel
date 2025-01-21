import os
import zipfile

dir_path = os.path.expanduser("~/.local/bin")

if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    print(f"Directory {dir_path} created.")
else:
    print(f"Directory {dir_path} already exists.")

zip_files = ["pel.zip", "websrv.zip"]

for zip_file in zip_files:
    if os.path.exists(zip_file):
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(dir_path)
            print(f"Extracted {zip_file} to {dir_path}")
    else:
        print(f"{zip_file} not found in the current directory.")
