import webbrowser
import json
from urllib.request import urlopen

print("let's find old website")
site=input("type URL: ")
era=input("type year, month, day, like 20151012: ")
url="https://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site=data["archieved snapshot"]["closest"]["url"]
    print("found this copy: " , old_site)
    print("appear on browser")
    webbrowser.open(old_site)
except:
    print("sorry no luck finding" , site)



