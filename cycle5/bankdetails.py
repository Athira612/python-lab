class Bank:
    def __init__(self):
        self.balance = 0

        n = input("Enter the name:")
        a = int(input("Enter the account number:"))
        t = input("Enter the type of account:")
        print("Hello", n, " Welcome To SBI")

    def deposit(self):
        amount = float(input("Enter the amount  to be deposited:"))
        self.balance += amount
        print("Amount diposited Sucessfully")
        print("Avilabile balance is", amount)

    def withdraw(self):
        amount = float(input("Enter the amount to be withdraw:"))
        if self.balance >= amount:
             self.balance -= amount
             print("You Withdrew", amount)
        else:
             print("Insufficient Balance")


    def display(self):
        print("Avilable balance is ", self.balance)


s = Bank()
s.deposit()
s.withdraw()
s.display()
