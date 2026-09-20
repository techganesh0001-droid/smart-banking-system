class BankAccount:

    def __init__(self, name, account_no, pin):
        self.name = name
        self.account_no = account_no
        self.pin = pin
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited ₹{amount}")
            print("Money deposited successfully.")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Not enough balance.")
        else:
            self.balance -= amount
            self.history.append(f"Withdrawn ₹{amount}")
            print("Money withdrawn successfully.")

    def show_balance(self):
        print("Your balance is ₹", self.balance)

    def show_history(self):
        if len(self.history) == 0:
            print("No transactions yet.")
        else:
            print("\nTransaction History")
            for item in self.history:
                print(item)


accounts = {}

while True:

    print("\n===== MY BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter your name: ")
        account_no = input("Create account number: ")
        pin = input("Create PIN: ")

        if account_no in accounts:
            print("Account already exists.")
        else:
            accounts[account_no] = BankAccount(
                name, account_no, pin
            )
            print("Account created successfully!")

    elif choice == "2":

        account_no = input("Enter account number: ")

        if account_no not in accounts:
            print("Account not found.")
            continue

        account = accounts[account_no]

        pin = input("Enter PIN: ")

        if pin != account.pin:
            print("Wrong PIN.")
            continue

        print("\nWelcome,", account.name)

        while True:

            print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Transaction History
5. Logout
""")

            option = input("Choose option: ")

            if option == "1":
                amount = float(input("Enter amount: ₹"))
                account.deposit(amount)

            elif option == "2":
                amount = float(input("Enter amount: ₹"))
                account.withdraw(amount)

            elif option == "3":
                account.show_balance()

            elif option == "4":
                account.show_history()

            elif option == "5":
                print("Logged out.")
                break

            else:
                print("Invalid option.")

    elif choice == "3":
        print("Thank you for using my banking system!")
        break

    else:
        print("Please enter a valid choice.")
