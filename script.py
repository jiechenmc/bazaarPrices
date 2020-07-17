import requests
import datetime


class BazaarData:
    def __init__(self):
        self.resp = requests.get(
            "https://api.hypixel.net/skyblock/bazaar?key=191e62a6-2d3e-49b1-b58e-106f0e16bb1f"
        ).json()

        self.products = self.resp["products"].keys()

    def get_lastUpdated(self):
        """ Returns when the response was last updated """
        unix_time = self.resp["lastUpdated"] / 1000
        real_time = datetime.datetime.fromtimestamp(unix_time).strftime(
            "%Y-%m-%d %H:%M:%S")
        return real_time

    def get_productStatus(self):
        """ Returns a generator filled with the status of every item """
        for product in self.products:
            yield self.resp["products"][product]

    def get_productQuickStatus(self):
        """ Returns a generator filled with the quick status of every item """
        for product_status in self.get_productStatus():
            yield product_status["quick_status"]


if __name__ == "__main__":
    data = BazaarData()
    for item in data.get_productQuickStatus():
        print(item)