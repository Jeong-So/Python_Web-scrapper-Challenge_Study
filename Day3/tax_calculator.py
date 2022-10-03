# Write your code here:

# Don't touch anthing below this line 🙅🏻‍♂️🙅🏻‍♀️

monthly_revenue = 5500000
monthly_expenses = 2700000
tax_credits = 0.01


def get_yearly_revenue(monthly_revenue=6000000):
    return monthly_revenue * 12


def get_yearly_expenses(monthly_expenses=2000000):
    return monthly_expenses * 12


def get_tax_amount(profit=4000000):
    if profit > 100000:
        return profit * 0.25
    else:
        return profit * 0.15


def apply_tax_credits(tax_amount=300000, tax_credits=0.02):
    return tax_amount * tax_credits


profit = get_yearly_revenue(monthly_revenue) - get_yearly_expenses(
    monthly_expenses)

tax_amount = get_tax_amount(profit)

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")
