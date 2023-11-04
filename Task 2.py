import sys
from collections import defaultdict
import numpy as np


def get_monthlys():
    " Places inputs as list of tuples (month, amount) "
    inputs = []

    while True:
        input_val = input("Month (1-12) and income or expense (space separated): ")
        if input_val == "":
            break
        month, amount = input_val.split()
        month, amount = int(month), float(amount)
        inputs.append((month, amount))

    return inputs


def groupby_month(inputs):
    " Groups cash flow for each month "
    cashflow = defaultdict(list)
    for month, amount in inputs:
        cashflow[month].append(amount)

    return cashflow


def show_monthlys(cashflow):
    s = sorted(cashflow.items(), key=lambda x: x[0])
    for month, amounts in s:
        incomes = [v for v in amounts if v >= 0]
        expenses = [-v for v in amounts if v < 0]
        net = sum(incomes) - sum(expenses)
        print(f'Month: {month}')
        print(f'Incomes: {" ".join(map(str, incomes)) if incomes else None}')
        print(f'Expenses: {" ".join(map(str, expenses)) if expenses else None}')
        print(f'Net for Month: {net}')
        print()


def calculate_npv(interest_rate, cashflow):
    " NPV "
    min_month, max_month = min(cashflow.keys()), max(cashflow.keys())

    totals = np.zeros(max_month - min_month + 1, dtype='f')

    for month, amounts in cashflow.items():
        month_index = month - min_month
        totals[month_index] = sum(amounts)

    return np.npv(interest_rate, totals)


# Get inputs
rate_input = input("Monthly Interest rate: ")
try:
    interest_rate = float(rate_input)
except ValueError:
    print("Error-->> interest rate should be numeric")
    sys.exit()

inputs = get_monthlys()
cashflow = groupby_month(inputs)

# Monthly Reports
show_monthlys(cashflow)

# Net Present Value
print(f'Net Present Value: {calculate_npv(interest_rate, cashflow):.2f}')
