import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import string
import json
import requests


def _getVanilla():
    url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
    downloadUrl = 'https://s3.amazonaws.com/Minecraft.Download/versions/:VERSION:/minecraft_server.:VERSION:.jar'
    f = json.loads(requests.get(url).text)

    versions = []
    for v in f['versions']:
        if v['type'] == 'release' and v['releaseTime'] > "2014-03-25":
            versions.append({'id': v['id'], 'url': downloadUrl.replace(':VERSION:', v['id'])})
    for v in f['versions']:
        if v['type'] == 'snapshot' and v['releaseTime'] > "2014-03-25":
            versions.append({'id': v['id'], 'url': downloadUrl.replace(':VERSION:', v['id'])})

    return versions


def _getCraftBukkit():
    craftbukkit = []
    url = "https://getbukkit.org/download/craftbukkit"
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent':user_agent,}
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    text = response.read()
    soup = BeautifulSoup(text)

    data = soup.findAll('div', class_="download-pane")

    for div in data:
        version = str(div.find('div', class_='col-sm-3')).split('\n')[2][4:-5]


def getVersions():
    vanilla = _getVanilla()
    craftbukkit = _getCraftBukkit()
    spigot = ''
    papermc = ''



    print('vanilla', craftbukkit, spigot, papermc, sep='\n')
    return {'Vanilla': vanilla, 'CraftBukkit': craftbukkit,
            'Spigot': spigot, 'PaperMC': papermc}

chars = list(string.ascii_lowercase)
final = getVersions()
