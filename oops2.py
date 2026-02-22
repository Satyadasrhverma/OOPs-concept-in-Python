#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance.

class Bank:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def debit(self, amount):
        if amount <= 0:
            print("Invalid debit amount")
            return

        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount
        print(f"Rs {amount} debited")
        print(f"Total balance = {self.balance}")

    def credit(self, amount):
        if amount <= 0:
            print("Invalid credit amount")
            return

        self.balance += amount
        print(f"Rs {amount} credited")
        print(f"Total balance = {self.balance}")

    def get_balance(self):
        return self.balance


acc_num = int(input("Enter a account number :"))
balance = int(input("Enter balance"))
acc1 = Bank(acc_num , balance)

while True:
    print ("1.debit")
    print("2.credit")
    print("3.Check Balance")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = int(input("Enter debit amount: "))
        acc1.debit(amount)

    elif choice == 2:
        amount = int(input("Enter credit amount: "))
        acc1.credit(amount)

    elif choice == 3:
        print("Current balance:", acc1.get_balance())

    else:
        print("Invalid choice")



