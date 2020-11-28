import requests
import json

versions = []
link = "https://archive.mcmirror.io/Spigot/"
f = json.loads(requests.get(link).text)
