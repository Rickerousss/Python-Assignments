class SavingsAccount:
    # constructor func
    def __init__(self, account_id: int,
                 balance: float,
                 previous_balance: float,
                 annual_interest_rate: float):
        self.account_id = account_id
        self.balance = balance
        self.previous_balance = previous_balance
        self.annual_interest_rate = annual_interest_rate

    # setters - func
    def set_interest_rate(self, updated_interest_rate):
        self.annual_interest_rate = updated_interest_rate

    # getters
    def get_monthly_interest_rate(self):
        return self.annual_interest_rate / 12 / 100

    def get_monthly_interest(self):
        return self.balance * self.get_monthly_interest_rate()

    def get_balance_change_percent(self):
        return ((self.balance - self.previous_balance) / self.previous_balance) * 100

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance = self.balance - amount

    def deposit(self, amount: float) -> None:
        self.balance = self.balance + amount


# entry func
def main():
    account = SavingsAccount(1122, 20_000.0, 18_500.0, 4.5)

    account.withdraw(2_500.0)
    account.deposit(3_000.0)

    print(f"Account id: {account.account_id}")
    print(f"Current balance: {account.balance}")
    print(f"Monthly interest rate: {account.get_monthly_interest_rate() * 100}%")
    print(f"Monthly interest: {account.get_monthly_interest():.2f}")
    print(f"Percentage change: {account.get_balance_change_percent():.2f}%")


if __name__ == "__main__":
    main()
