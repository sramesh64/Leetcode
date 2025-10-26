class Bank:

    def __init__(self, balance: List[int]):
        self.balances = balance
        self.num_accounts = len(self.balances)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (not(1 <= account1 <= self.num_accounts and 1 <= account2 <= self.num_accounts)):
            return False
        if(money > self.balances[account1 - 1]):
            return False
        self.balances[account1 - 1] -= money
        self.balances[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if (not(1 <= account <= self.num_accounts)):
            return False
        self.balances[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if (not(1 <= account <= self.num_accounts)):
            print("hi")
            return False
        if(money > self.balances[account - 1]):
            print("hi2")
            return False
        self.balances[account - 1] -= money  
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)