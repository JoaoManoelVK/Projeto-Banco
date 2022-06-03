from conta import Account


class savings(Account):
    def __init__(self, name, cpf, address, number, overdraft):
        super().__init__(name, cpf, address, number, overdraft)
        taxes = 0.0017