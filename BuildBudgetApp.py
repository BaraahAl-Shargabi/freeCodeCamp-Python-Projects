class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append({'amount': self.amount, 'description': self.description})

    def withdraw(self, amount,description=""):
        self.amount = amount
        self.description = description
        if self.check_funds(self.amount):
            self.ledger.append({'amount': 0-self.amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        output = ""

        for item in self.ledger:
            description = item["description"][:23]
            amount = item["amount"]
            amount_formatted = f"{amount:.2f}"
            line = description.ljust(23) + amount_formatted.rjust(7)
            output += line + "\n"

        output += f"Total: {self.get_balance():.2f}"
        return title + output


def create_spend_chart(categories):
    pass