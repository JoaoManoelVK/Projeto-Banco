from conta import Account

class Checking(Account):

    def __init__(self, name, cpf, address, number, overdraft):
        super().__init__(name, cpf, address, number, overdraft)
        