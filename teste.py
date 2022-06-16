from email.mime import base
from tomlkit import string


baseurl = 'https://c44c-2804-ec8-18-2718-2854-71a4-96f-2.sa.ngrok.io'

import requests

myobj = {'cpf': '12345678909','senha': '123456'}

x = requests.post(baseurl+'/auth',json=myobj)
print(x.json()['token'])