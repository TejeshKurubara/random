class Account:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance

    def deposit(self):
        amount = float(input("Enter Deposit Amount: "))
        self.__balance += amount
        print("Amount Deposited Successfully")

    def withdraw(self):
        amount = float(input("Enter Withdraw Amount: "))

        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    def display(self):
        print("\nAccount Number :", self.acc_no)
        print("Name :", self.name)
        print("Balance :", self.__balance)

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount


class SavingsAccount(Account):
    def account_type(self):
        print("Savings Account")


class CurrentAccount(Account):
    def account_type(self):
        print("Current Account")


accounts = []

while True:

    print("\n===== BANK MANAGEMENT =====")
    print("1.Create Account")
    print("2.Display Accounts")
    print("3.Deposit")
    print("4.Withdraw")
    print("5.Exit")

    ch = int(input("Enter Choice: "))

    if ch == 1:

        acc = input("Enter Account Number: ")
        name = input("Enter Name: ")
        bal = float(input("Enter Balance: "))

        print("1.Savings")
        print("2.Current")

        t = int(input("Choose Account Type: "))

        if t == 1:
            obj = SavingsAccount(acc, name, bal)
        else:
            obj = CurrentAccount(acc, name, bal)

        accounts.append(obj)
        print("Account Created Successfully")

    elif ch == 2:

        if len(accounts) == 0:
            print("No Accounts Found")

        else:
            for a in accounts:
                a.display()

    elif ch == 3:

        acc = input("Enter Account Number: ")

        found = False

        for a in accounts:
            if a.acc_no == acc:
                a.deposit()
                found = True
                break

        if found == False:
            print("Account Not Found")

    elif ch == 4:

        acc = input("Enter Account Number: ")

        found = False

        for a in accounts:
            if a.acc_no == acc:
                a.withdraw()
                found = True
                break

        if found == False:
            print("Account Not Found")

    elif ch == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")
