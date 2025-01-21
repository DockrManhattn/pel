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

shell = os.environ.get('SHELL', '').lower()
alias_command = "alias pel='python3 ~/.local/bin/pel/pel.py'\nalias pelw='python3 ~/.local/bin/pel/pelw.py'"

if "bash" in shell:
    rc_file = os.path.expanduser("~/.bashrc")
elif "zsh" in shell:
    rc_file = os.path.expanduser("~/.zshrc")
else:
    print(f"Unsupported shell: {shell}")
    rc_file = None

if rc_file:
    with open(rc_file, 'a') as f:
        f.write("\n" + alias_command + "\n")
    print(f"Added aliases to {rc_file}")

