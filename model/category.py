from re import L
from model.account import account

class category:
    def __init__(self, name):
        self.accounts = {}
        self.name = name

    def add_entry(self, entry):
        if entry.name not in self.accounts:
            self.accounts[entry.name] = account(entry.name)
        self.accounts[entry.name].add_entry(entry)

    def contains(self, account):
        return account in self.accounts

    def get_account(self, name):
        return self.accounts[name]
            
    def print_category(self):
        print(self.name.upper())
        for account in self.accounts.keys():
            self.accounts[account].print_account()