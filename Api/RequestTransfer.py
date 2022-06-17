import RequestApi


def deposit(token, origem, destino, valor):
    headers = { "Authorization": token }
    payload = {
  	  "origem": origem,
	  "destino": destino,
	  "valor": valor
    }
    return RequestApi.post("/transacoes/transferencia", json=payload, headers=headers)
