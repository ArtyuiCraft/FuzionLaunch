import subprocess
from os import remove

def menu(options=[1, 2, 3]):
    with open("temp.txt", "w") as f:
        for i in options: f.write(str(i) + "\n")
    result = subprocess.run(['fzf'], stdin=open("temp.txt"), stdout=subprocess.PIPE, text=True)
    remove("temp.txt")
    if result.returncode == 0: return result.stdout.strip()
    else: return None
