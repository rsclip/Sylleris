import requests
import json

versions = []
link = "https://yivesmirror.com/api/list/paper"
f = json.loads(requests.get(link).text)
f.sort()
for version in f:
    versions.append({'id': version.replace('Paper-', ''),
                     'url': f'https://yivesmirror.com/files/paper/{version}'})
print(json.dumps(versions,indent=4))
