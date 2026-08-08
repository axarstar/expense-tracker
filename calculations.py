import numpy as np


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

def get_statistics(expenses):
    amounts = get_all_amounts(expenses)
    if not amounts:
        return {
            "Average": 0,
            "Maximum": 0,
            "Minimum": 0
        }
    avg = np.mean(amounts)
    max_amount = np.max(amounts)
    min_amount = np.min(amounts)

    return {
        "Average": avg,
        "Maximum": max_amount,
        "Minimum": min_amount
    }