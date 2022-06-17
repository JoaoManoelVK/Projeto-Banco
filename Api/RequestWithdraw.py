import RequestApi


def withdraw(token, conta, valor):
    headers = { "Authorization": token }
    payload = {
	  "conta": conta,
	  "valor": valor
    }
    return RequestApi.post("/transacoes/saque", json=payload, headers=headers)
