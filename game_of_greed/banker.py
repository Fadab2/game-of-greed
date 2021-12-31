class Banker:
    def __init__(self, shelved=0, balance=0):
        self.shelved = shelved
        self.balance = balance

    def shelf(self, num):
        self.shelved += num
    
    def bank(self):
        self.balance += self.shelved #incrememented balance
        self.shelved = 0
        return self.balance

    def clear_shelf(self):
        self.shelved = 0
