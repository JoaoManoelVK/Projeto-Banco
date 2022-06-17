import RequestApi


def deposit(token, conta, valor):
    headers = { "Authorization": token }
    payload = {
      "conta": conta,
	  "valor": valor
    }
    return RequestApi.get("//transacoes/deposito", json=payload, headers=headers)
