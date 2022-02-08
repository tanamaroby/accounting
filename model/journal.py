# This class contains all journal entries categorized by accounts
from model.entry import entry
from model.account import account
from model.category import category

class journal:

    def __init__(self):
        self.journal = {}

    def store_journal(self, name, cat, is_debit, value, time):
        new_entry = entry(name, is_debit, value, time)

        # Storing in specific account types
        if cat not in self.journal:
            self.journal[cat] = category(cat)
        self.journal[cat].add_entry(new_entry)

    def print_journal(self):
        for category in self.journal.keys():
            self.journal[category].print_category()
