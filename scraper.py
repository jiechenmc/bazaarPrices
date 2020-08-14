from requests_html import HTMLSession
session = HTMLSession()
resp = session.get("https://hypixel-skyblock.fandom.com/wiki/Bazaar")
resp.html.render()
