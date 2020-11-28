import requests

url = 'https://yivesmirror.com/files/paper/Paper-1.15.2-b99.jar'
with open('server.jar', 'wb') as f:
    f.write(requests.get(url).content)
