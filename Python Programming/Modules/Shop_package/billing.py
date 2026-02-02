def calculate_total(prices):
    total = 0
    for i in range(len(prices)):
        total += prices[i]
    return total

def apply_tax(amount):
    return amount + amount * 0.05