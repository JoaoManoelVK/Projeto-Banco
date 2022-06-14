from Account import Account


class savings(Account):
    def __init__(self, name, cpf, address, number, balance, overdraft):
        super().__init__(name, cpf, address, number, balance, overdraft)
        taxes = 0.0017

        def taxas(self):
            self.__balance =  self.__balance + (self.__balance * taxes) 
