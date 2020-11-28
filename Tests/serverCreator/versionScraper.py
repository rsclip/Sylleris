import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import string
import json
from threading import Thread


def _getVanilla():
    def _vanillaGetDirect(url):
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers = {'User-Agent':user_agent,}
        request = urllib.request.Request(url, None, headers)
        response = urllib.request.urlopen(request)
        text = response.read()
        soup = BeautifulSoup(text)
        data = soup.findAll('a', class_="button")
        direct = data[0]['href']
        vanilla[a['href'].split('/')[-1]] = _vanillaGetDirect("https://mcversions.net" + a['href'])

    vanilla = {}
    url = "https://mcversions.net/"
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent':user_agent,}
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    text = response.read()
    soup = BeautifulSoup(text)

    data = soup.findAll('div', class_="items")
    for div in data:
        links = div.findAll('a')
        for a in links:
            if a['href'].startswith('/download/') and '.' in a['href'] and not (a['href'].split('/')[-1][0] in chars):
                Thread(target=_vanillaGetDirect,args=("https://mcversions.net" + a['href'],)).start()

    return vanilla


def _getCraftBukkit():
    craftbukkit = {}
    url = "https://getbukkit.org/download/craftbukkit"
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent':user_agent,}
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    text = response.read()
    soup = BeautifulSoup(text)

    data = soup.findAll('div', class_="col-md-12 download")
    for div in data:
        metadiv = div.find('div', class_="col-sm-3")
        version = str(metadiv).split('<h2>')[-1].split('</h2>')[0]
        links = div.findAll('a')
        for a in links:
            if 'https://getbukkit.org/' in a['href']:
                craftbukkit[version] = a['href']
        print(craftbukkit)


def getVersions():
    vanilla = _getVanilla()
    craftbukkit = _getCraftBukkit()
    spigot = ''
    papermc = ''



    print(vanilla, craftbukkit, spigot, papermc, sep='\n')
    return {'Vanilla': vanilla, 'CraftBukkit': craftbukkit,
            'Spigot': spigot, 'PaperMC': papermc}

chars = list(string.ascii_lowercase)
final = getVersions()
print(json.dumps(final, indent=4))
