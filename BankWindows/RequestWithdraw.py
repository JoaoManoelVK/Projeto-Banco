import RequestApi


def withdraw(token, conta, valor):
    headers = { "Authorization": token }
    payload = {
    "conta": int(conta),
	  "valor": float(valor)
    }
    print(payload)
    return RequestApi.post("/transacoes/saque", json=payload, headers=headers)
