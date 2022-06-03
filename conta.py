from abc import ABC, abstractmethod
 
class Account(ABC):
 
    @abstractmethod
    def __init__(self, name, cpf, address, number, balance, overdraft):
        self.__name = name
        self.__cpf = cpf
        self.__address = address
        self.__number = number
        self.__balance = 0
        self.__overdraft = False
        self.__extract = list()

    def getName(self):
        return self.__name
      
    def setName(self, x):
        self.__name = x

    def getCpf(self):
        return self.__cpf
      
    def setCpf(self, x):
        self.__name = x

    def getAddress(self):
        return self.__address
      
    def setAddress(self, x):
        self.__address = x

    def getNumber(self):
        return self.__number
      
    def setNumber(self, x):
        self.__number = x

    def getNumber(self):
        return self.__number

    def getBalance(self):
        return self.__balance

    def setOverdraft(self, x):
        self.__overdraft = x
      
    def withdraw(self, x):
        if(x > 0):
            if(self.__overdraft == False):
                if(self.__balance < x):
                    print("Saldo Insuficiente")
                else:
                    self.__balance = self.__balance - x
                    self.__extract.append("Saque de " + str(x))
            else:
                self.__balance = self.__balance - x
                self.__extract.append("Saque de " + str(x))
        else:
            print("Valor Invalido")

    def deposit(self,x):
        if(x <= 0):
            print("Valor Invalido")
        else:
            self.__balance = x
            self.__extract.append("Deposito de " + str(x))


    def extract(self):
            print(self.__extract)