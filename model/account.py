class account:
    def __init__(self, name):
        self.entries = []
        self.name = name
        self.total = 0

    def add_entry(self, entry):
        self.total = self.total + entry.value
        self.entries.append(entry)

    def print_account(self):
        print(f"\t{self.name}")
        for entry in self.entries:
            print(f"\t\t{entry}")