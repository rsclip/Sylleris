import requests
import json

url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
f = json.loads(requests.get(url).text)

versions = []
for v in f['versions']:
    if v['type'] == 'release' and v['releaseTime'] > "2014-03-25":
        versions.append({'id': v['id'], 'url': v['url']})
for v in f['versions']:
    if v['type'] == 'snapshot' and v['releaseTime'] > "2014-03-25":
        versions.append({'id': v['id'], 'url': v['url']})

print(json.dumps(versions, indent=4))
