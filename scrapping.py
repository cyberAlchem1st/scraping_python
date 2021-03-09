# lxml 
# requests

with open('links.txt', 'r') as f:
   lista = f.read(-1).split("\n")

import requests
from lxml import html

for item in lista: 
    req = requests.get(item)
    tree = html.fromstring(req.content)
    genero = tree.xpath('//*[@id="a-page"]/main/div/div[3]/div[4]/div[7]/span[2]/text()')
    generoStr = str(genero).replace("\\n    \\n        ", ' ').replace("['", '').replace("']", '')
    print(generoStr)