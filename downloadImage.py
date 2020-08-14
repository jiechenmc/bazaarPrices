import requests
import re
import shutil
import os

pattern = re.compile(r"[a-zA-z0-9]+\.png")
with open("sources.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        url = line
        file_name = re.search(pattern, line).group(0)
        r = requests.get(url)
        directory = "pics/"

        try:
            with open(directory + file_name, "wb") as f:
                shutil.copyfileobj(r.raw, f)
        except FileNotFoundError:
            os.mkdir(directory)
            with open(directory + file_name, "wb") as f:
                shutil.copyfileobj(r.raw, f)
        except:
            print(file_name)