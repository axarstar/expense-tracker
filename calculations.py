def get_total(expenses):
    total = 0
    for exp in expenses:
        total += exp.amount
    return total

def filter_by_category(expenses, category):
    filtered = list(filter(lambda exp: exp.category.lower() == category.lower(), expenses))
    return filtered

def get_all_amounts(expenses):
    amounts = list(map(lambda exp: exp.amount, expenses))
    return amounts
