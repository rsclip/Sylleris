import requests
import json

versions = []
link = "https://mcmirror.io/api/list/spigot"
f = json.loads(requests.get(link).text)
f.sort()
for version in f:
    versions.append({'id': version.replace('Spigot-', 'Spigot ').split('-')[0],
                     'url': f'https://mcmirror.io/files/spigot/{version}'})
versions = versions[::-1]
print(json.dumps(versions,indent=4))

for v in versions:
    print(f'{v["id"]}: {v["url"]}')
