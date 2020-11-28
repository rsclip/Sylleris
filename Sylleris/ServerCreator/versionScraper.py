import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import string
import json
import requests
import calendar


def _getVanilla():
    url = "https://launchermeta.mojang.com/mc/game/version_manifest.json"
    f = json.loads(requests.get(url).text)

    versions = []
    for v in f['versions']:
        if v['type'] == 'release' and v['releaseTime'] > "2014-03-25":
            versions.append({'id': v['id'], 'url': v['url']})

    for v in f['versions']:
        if v['type'] == 'snapshot' and v['releaseTime'] > "2019-03-25":
            versions.append({'id': v['id'], 'url': v['url']})

    return versions


def _getCraftBukkit():
    versions = []
    link = "https://mcmirror.io/api/list/craftbukkit"
    f = json.loads(requests.get(link).text)
    f.sort()
    for version in f:
        if not version == 'craftbukkit-latest.jar':
            versionSplit = version.split('-')
            date = f"{versionSplit[3][:4]}/{versionSplit[3][4:6]}/{versionSplit[3][6:]}"
            versionID = versionSplit[1]
        else:
            date = 'Latest'
            versionID = version
        if date > "2019/08/01":
            versions.append({'id': versionID + f' ({date})',
                             'url': f'https://mcmirror.io/files/craftbukkit/{version}',
                             'date': date})
    versions = sorted(versions, key=lambda k: k['date'])[::-1]
    return versions


def _getPaper():
    versions = []
    link = "https://yivesmirror.com/api/list/paper"
    f = json.loads(requests.get(link).text)
    f.sort()
    for version in f:
        versions.append({'id': version.replace('Paper-', '').strip('.jar'),
                         'url': f'https://yivesmirror.com/files/paper/{version}'})

    return versions[::-1]


def _getSpigotExtra():
    versions = []
    link = "https://archive.mcmirror.io/Spigot/"
    f = requests.get(link).text.split('\n')[4:-3]
    for i in f:
        if (not 'api' in i) and (not 'spigot-latest' in i):
            name = i.split('"')[1].strip('spigot-').strip('.jar')
            versions.append({
                'id': name,
                'url': 'https://archive.mcmirror.io/Spigot/' + i.split('"')[1],
                'date': 'Archived'})

    versions = sorted(versions, key=lambda k: k['id'])[::-1]
    return versions


def _getSpigot():
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
    extraVersions = _getSpigotExtra()
    for v in extraVersions:
        versions.append(v)
    return versions


def getVersions():
    vanilla = _getVanilla()
    craftbukkit = _getCraftBukkit()
    spigot = _getSpigot()
    papermc = _getPaper()
    forge = []

    return {'Vanilla': vanilla, 'CraftBukkit': craftbukkit,
            'Spigot': spigot, 'PaperMC': papermc, 'Forge': forge}

chars = list(string.ascii_lowercase)
monthabbr = {v: k for k,v in enumerate(calendar.month_abbr)}
