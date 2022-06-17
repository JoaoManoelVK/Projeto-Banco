import RequestApi


def extract(token, conta):
    headers = { "Authorization": token }
    return RequestApi.get("/transacoes/extrato/"+str(conta),headers=headers)
