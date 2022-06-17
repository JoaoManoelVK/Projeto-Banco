import RequestApi


def deposit(token, conta):
    headers = { "Authorization": token }
    return RequestApi.get("/transacoes/extrato"+conta, json=payload, headers=headers)
