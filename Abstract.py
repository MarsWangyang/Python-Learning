from abc import ABCMeta, abstractmethod
# python裡面沒有abstract 或是 interface
# 因此想變成Abstract class就得需要metaclass = ABCMeta
# 想變成interface的話，就加上@abstractmethod
# 概念：以下舉例

# Account此class是一個object，代表仍可以被instantiated
# 但是可以見到如果今天只創建這個Account的話，self.id．．．都是沒有attributes能夠輸入
# 因此必定會錯誤
# 換想法=> 我們不應該會直接去建立一個模糊的帳號，應該是要利用繼承去給每個定義好功能的account去特異化
# 因此應該要把account變成抽象的概念
# ----------------改--------------------
# class Account(metaclass=ABCMeta):
#    ...
#    @staticmethod
#    def

class Account():
    def withdraw(self, amount):
        if amount >= self.balance:
            self.balance -= amount
        else:
            raise ValueError('餘額不足')

    def __str__(self):
        return ('Id:\t\t' + self.id +
               '\nName:\t\t' + self.name +
               '\nBalance:\t' + str(self.balance))


class CheckingAccount(Account):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.balance = 0
        self.overdraftlimit = 30000

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraftlimit:
            self.balance -= amount
        else:
            raise ValueError('超出信用')

    def __str__(self):
        return (super(CheckingAccount, self).__str__() +
                '\nOverdraft limit\t' + str(self.overdraftlimit));


acct = CheckingAccount('E1223', 'Justin Lin')
print(acct)


