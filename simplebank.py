class Account:
    def __init__(self, name, account_num, balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance
    
    def general(self):
        print(f"Name: {self.name}\nAccount number: {self.account_num}\nBalance: {self.balance}")
        
    def view_balance(self):
        print(f"Your balance: {self.balance}")
    
    def deposit(self, deposit):
        self.balance += deposit
        print(f"Balance: {self.balance}")
    def withdraw(self, withdrawal):
        if (self.balance <= 0) or\
            (self.balance <withdrawal):
            print("Unable to process transaction")
        else: 
            self.balance -= withdrawal
            print(f"Balance: {self.balance}")

person = Account("Johnny", "5420", 200)

person.general()
while True:
    options = input(f"View balance [1] Make a deposit [2] Make a withdrawal [3]\n> ")
    if options == "1":
        person.view_balance()
    elif options == "2":
        deposit_amount = int(input("Enter amount to deposit: "))
        person.deposit(deposit_amount)
    elif options == "3":
        withdrawal_amount = int(input("enter amount to withdraw: "))
        person.withdraw(withdrawal_amount)
    else:
        break