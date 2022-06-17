import requests


baseurl = "http://localhost:3000"


class RequestAuth(Exception):
    def auth(cpf, senha):
        payload = { 'cpf': cpf, 'senha': senha }
        request = requests.post(baseurl+"/auth", json=payload)
