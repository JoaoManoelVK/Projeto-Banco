import RequestApi


def deposit(token, conta, valor):
    headers = { "Authorization": token }
    payload = {
    "conta": int(conta),
	"valor": float(valor)
    }

    print(payload)
    return RequestApi.post("/transacoes/deposito", json=payload, headers=headers)
