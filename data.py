from pymongo import MongoClient
cluster = MongoClient(
    "mongodb+srv://ESSAY:dUe5KbPiaNsueEOb@cluster0.rqx0c.mongodb.net/BazaarStats?retryWrites=true&w=majority"
)
db = cluster["BazaarStats"]
collection = db["stats"]
results = collection.find()

with open("data.csv", "w") as f:
    f.write("lastUpdated,item,buyPrice,sellPrice")
    for result in results:
        lu = result["lastUpdated"]
        item = result["itemName"]
        bp = result["buyPrice"]
        sp = result["sellPrice"]
        f.write(f"\n{lu},{item},{bp},{sp}")