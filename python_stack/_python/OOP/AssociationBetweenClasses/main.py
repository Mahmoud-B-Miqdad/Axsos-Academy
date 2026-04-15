from User import User
from BankAccount import BankAccount

print("="*20)
print("BANK ACCOUNT TESTS")
print("="*20)

acc1 = BankAccount(0.02, 100) 
acc2 = BankAccount(0.05, 500) 

print("--- Account 1 Transactions ---")
acc1.deposit(50).deposit(100).deposit(50).withdraw(80).yield_interest().display_account_info()

print("\n--- Account 2 Transactions ---")
acc2.deposit(200).deposit(300).withdraw(100).withdraw(50).withdraw(50).withdraw(100).yield_interest().display_account_info()


print("\n" + "="*25)
print("USER WITH ACCOUNT TESTS")
print("="*25)

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