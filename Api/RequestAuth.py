import RequestApi


def auth(cpf, senha):
    payload = {
      'cpf': cpf,
      'senha': senha
    }
    return RequestApi.post("/auth", json=payload)
