from conta import Account

class Checking(Account):

    def __init__(self, name, cpf, address, number, overdraft):
        super().__init__(name, cpf, address, number, overdraft)
        

conta = Checking('Joao Manoel',12312312,'Canoa Quebrada',88988850201,False)
conta.deposit(30)
conta.withdraw(40)
conta.set_overdraft(True)
conta.withdraw(40)
conta.extract()
print(conta.get_balance())