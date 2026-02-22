class Phone:
    def __init__(self, price , brand , camera):
        print("INSIDE PHONE")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self) :
        print("Buying a phone")   

class Smartphone(Phone):
    def buy(self):
        print("INSIDE SMARTPHONE")\


s = Smartphone(10000, "OPPO", 23)
s.buy()