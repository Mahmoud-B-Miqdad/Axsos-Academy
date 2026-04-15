class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
        else:
            print(f"Sorry {self.name}, the balance is insufficient to withdraw ${amount}")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        if amount <= self.account_balance:
            print(f"--- Transferring ${amount} from {self.name} to {other_user.name} ---")
            self.account_balance -= amount
            other_user.account_balance += amount
            self.display_user_balance()
            other_user.display_user_balance()
        else:
            print(f"Transfer failed: {self.name}'s balance is insufficient.")
        return self

mahmoud = User("Mahmoud Miqdad", "Mahmoud.Miqdad@axsos.academy")
monty = User("Monty Python", "monty@python.com")
jack = User("Jack Sparrow", "jack@blackpearl.com")

print("--- User 1's Transactions ---")
mahmoud.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(45).display_user_balance()

print("\n--- User 2's Transactions ---")
monty.make_deposit(500).make_deposit(500).make_withdrawal(150).make_withdrawal(100).display_user_balance()

print("\n--- User 3's Transactions ---")
jack.make_deposit(1000).make_withdrawal(200).make_withdrawal(200).make_withdrawal(100).display_user_balance()

print("\n--- Bonus: Transfer from User 1 to User 3 ---")
mahmoud.transfer_money(jack, 150)