class entry:
    def __init__(self, name, is_debit, value, time):
        self.name = name
        self.is_debit = is_debit
        self.value = value
        self.time = time

    def __str__(self):
        account_type = "Debit" if self.is_debit else "Credit"
        return f"{account_type} {self.name} with value {self.value} at time {self.time}"