import requests

with open("sources.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        print(line)