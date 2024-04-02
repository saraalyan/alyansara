class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)


class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def transfer(self, source_account_number, destination_account_number, amount):

            if source_account_number.balance >= amount:
                source_account_number.balance -= amount
                destination_account_number.balance += amount
                print("Transfer successful.")
            else:
                print("not support")



bank = Bank("Example Bank")

customer1 = Customer("Alice")
customer2 = Customer("Bob")

account1 = Account("1", 1000)
account2 = Account("2", 500)

customer1.add_account(account1)
customer2.add_account(account2)

bank.add_customer(customer1)
bank.add_customer(customer2)

print("Bank Name:", bank.name)
for customer in bank.customers:
    print("Customer:", customer.name)
    print("Accounts:")
    for account in customer.accounts:
        print("Account Number:", account.account_number)
        print("Balance:", account.get_balance())
customer1.transfer("1", "2", 200)
for account in customer1.accounts:
    print("Account Number:", account.account_number)
    print("Balance:", account.get_balance())
