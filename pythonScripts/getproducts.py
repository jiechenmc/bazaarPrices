import requests

r = requests.get(
    "https://api.hypixel.net/skyblock/bazaar?key=191e62a6-2d3e-49b1-b58e-106f0e16bb1f"
).json()

products = [product + "\n" for product in r["products"]]
products[-1] = products[-1].replace("\n", "")

with open("../products.txt", "w") as f:
    f.writelines(products)