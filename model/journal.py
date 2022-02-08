# This class contains all journal entries categorized by accounts
import database.account_types as at
from model.entry import entry
from model.account import account
from model.category import category

class journal:

    def __init__(self):
        self.journal = {}
        self.journal[at.get_assets()] = category(at.get_assets())
        self.journal[at.get_liabilities()] = category(at.get_liabilities())
        self.journal[at.get_equity()] = category(at.get_equity())

    def store_journal(self, name, is_debit, value, time):
        new_entry = entry(name, is_debit, value, time)

        # Storing in specific account types
        account_type = at.get_account_type(name.lower())
        self.journal[account_type].add_entry(new_entry)

    def print_journal(self):
        for category in self.journal.keys():
            self.journal[category].print_category()
