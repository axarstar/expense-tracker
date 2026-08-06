class expense:

    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"Amount: {self.amount}, Category: {self.category}, Description: {self.description}"


class recurringExpense(expense):

    def __init__(self, amount, category, description, frequency):
        super().__init__(amount, category, description)
        self.frequency = frequency

    def __str__(self):
        super_str = super().__str__()
        return f"{super_str}, Frequency: {self.frequency}"
    