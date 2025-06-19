class BankBalanceError(Exception):
    def __init__(self, balance, message="Insufficient funds!"):
        self.balance = balance
        self.message = message
        super().__init__(self.message)
        
def withdraw(amount, balance):
    if amount > balance:
        raise BankBalanceError(balance, f"Available balance is only ${balance}")
    return f"Withdrawal of {amount} seuccessful!"

try:
    current_balance = 1000
    amount_to_withdraw = int(input("Enter amount to withdraw: "))
    print(withdraw(amount_to_withdraw, current_balance))
except BankBalanceError as e:
    print(f"Transaction Failed: {e.message}")
except ValueError:
    print("Invalid input: Please enter a number.")
finally:
    print("Bank transaction Coompleated")