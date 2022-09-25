"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 1.1
else:
    bonus = sales * 1.15
print(bonus - sales)
print(f"Your bonus on {sales} is ${(bonus - sales):.1f}")
