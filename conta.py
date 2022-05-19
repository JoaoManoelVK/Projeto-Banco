from abc import ABC, abstractmethod
 
class Account(ABC):
 
    @abstractmethod
    def __init__(self, name, cpf, address, number, overdraft):
        self.__name = name
        self.__cpf = cpf
        self.__address = address
        self.__number = number
        self.__balance = 0
        self.__overdraft = False

    def get_name(self):
        return self.__name
      
    def set_name(self, x):
        self.__name = x

    def get_cpf(self):
        return self.__cpf
      
    def set_cpf(self, x):
        self.__name = x

    def get_address(self):
        return self.__address
      
    def set_address(self, x):
        self.__address = x

    def get_number(self):
        return self.__number
      
    def set_number(self, x):
        self.__number = x

    def get_number(self):
        return self.__number

    def get_balance(self):
        return self.__balance

    def set_overdraft(self, x):
        self.__overdraft = x
      
    def withdraw(self, x):
        if(x > 0):
            if(self.__overdraft == False):
                if(self.__balance < x):
                    print("Saldo Insuficiente")
                else:
                    self.__balance = self.__balance - x
        else:
            print("Valor Invalido")

    def deposit(self,x):
        if(x <= 0):
            print("Valor Invalido")
        else:
            self.__balance = x