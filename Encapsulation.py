#ENCAPSULATION IN OOP
class Bankaccount:
    def __init__(self,name,age,balance):
        self.name = name
        self._age = age
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposite(self,amount):
        self.__balance+=amount
        return f"Successfully deposite and current balance is {self.balance}"
    def withdraw(self,amount):
        if self.get_balance()>=amount:
            self.__balance-=amount
            return f"Successfully withdraw and current balance is {self.get_balance}"
        
obj= Bankaccount("Roma",21,1000)
print(obj.name)
print(obj._age)
print(obj._Bankaccount__balance)
print(obj.withdraw(500))
print(obj.get_balance())
    
