from requests_html import HTMLSession
import re

session = HTMLSession()
resp = session.get("https://hypixel-skyblock.fandom.com/wiki/Bazaar")
resp.html.render(scrolldown=1, timeout=100)

table = resp.html.find(".wikitable", first=True)
tds = table.find("tr > td")
sources = []

for td in tds:
    images = td.find(
        "a > img"
    )  # There are also <noscript> tags with <img> tags so this is nesscary as the <img> that I want is in the <a> tag
    for image in images:
        source = re.sub(
            r"\/revision.+", "", image.attrs["data-src"]
        )  # Remove /revision.+ so the iamge will always be its original size 430x430
        sources.append(source + "\n")
with open("pythonScripts/sources.txt", "w") as f:
    sources[-1] = sources[-1].replace("\n", "")
    f.writelines(sources)