import requests
import json
import calendar
from bs4 import BeautifulSoup as BS

import traceback

monthabbr = {v: k for k,v in enumerate(calendar.month_abbr)}

versions = []
link = "https://archive.mcmirror.io/Spigot/"
f = requests.get(link).text.split('\n')[4:-3]
for i in f:
    if (not 'api' in i) and (not 'spigot-latest' in i):
        name = i.split('"')[1].strip('spigot-').strip('.jar')
        versions.append({
            'name': name,
            'url': 'https://archive.mcmirror.io/Spigot/' + i.split('"')[1],
            'date': 'Archived'})

versions = sorted(versions, key=lambda k: k['name'])[::-1] 
print(json.dumps(versions, indent=4))
