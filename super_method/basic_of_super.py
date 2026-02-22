class Phone:
    def __init__(self, price ,name, brand):
        print("Inside PHONE")
        self.name = name
        self.__price = price
        self.brand = brand

    def buy(self):
        print("BUY a Phone")    

class OPPO(Phone):        
    def buy(self):
        print("Buy OPPO")
        super().buy() #---- call parent class buy method


a1 = OPPO(20000,"OPPO", 13)
a1.buy()


