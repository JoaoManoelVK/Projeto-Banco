import RequestApi


def listAccounts(token):
    headers = { "Authorization": token }
    return RequestApi.get("/contas", headers=headers)
