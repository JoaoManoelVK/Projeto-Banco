import RequestApi


def create(token, agencia, cpf, nome, email, telefone, endereco, senha):
    headers = { "Authorization": token }
    payload = {
      "conta": {
	    "agencia": 1
	  },
	  "titular": {
		"cpf": cpf,
		"nome": name,
		"email": email,
		"telefone": telefone,
		"endereco": endereco,
		"senha": senha
      }
	}
    return RequestApi.post("/contas/poupanca", json=payload, headers=headers)
