import requests
import datetime


class BazaarData:
    def __init__(self):
        self.resp = requests.get(
            "https://api.hypixel.net/skyblock/bazaar?key=191e62a6-2d3e-49b1-b58e-106f0e16bb1f"
        ).json()

    def get_lastUpdated(self):
        unix_time = self.resp["lastUpdated"] / 1000
        real_time = datetime.datetime.fromtimestamp(unix_time).strftime(
            "%Y-%m-%d %H:%M:%S")
        return real_time

    def get_productNames(self):
        return self.resp["products"]


if __name__ == "__main__":
    data = BazaarData()
    print(data.get_productNames())