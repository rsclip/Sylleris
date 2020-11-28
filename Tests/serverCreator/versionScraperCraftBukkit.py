import requests
import json

versions = []
link = "https://mcmirror.io/api/list/spigot"
f = json.loads(requests.get(link).text)
f.sort()
for version in f:
    if not version == 'spigot-latest.jar':
        versionSplit = version.split('-')
        date = f"{versionSplit[3][:4]}/{versionSplit[3][4:6]}/{versionSplit[3][6:]}"
        versionID = versionSplit[1]
    else:
        date = 'Latest'
        versionID = version
    versions.append({'id': versionID + f' ({date})',
                     'url': f'https://mcmirror.io/files/spigot/{version}',
                     'date': date})
versions = sorted(versions, key=lambda k: k['date'])[::-1] 
print(json.dumps(versions,indent=4))
