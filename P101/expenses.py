import pandas as pd
print(f"This is a Program for Expense tracker. Enter the category, price and date.")
expenses = []
while True:
    expense_data = {'Category': '', 'Price': '', 'Date': ''}
    category = input('Enter the category: ')
    price = float(input('Enter the price: '))
    date = input('Enter the date: ')
    expense_data = {'Category': category, 'Price': price, 'Date': date}
    expenses.append(expense_data)
    check = input('Do you have more expenses to add (y/n)?')
    if check.lower() =='n':
        break
    else:
        print('continue')
print(f'expenses are {expenses}')
category_total = {}
for each_expense in expenses:
        cat = each_expense['Category']
        price = each_expense['Price']
        category_total[cat] = category_total.get(cat,0) + price

print("\nTotal expenses by category:")
for category, total in category_total.items():
    print(f"{category}: ${total:.2f}")

df_expenses = pd.DataFrame(expenses)
df_totals = pd.DataFrame(list(category_total.items()), columns=['Category','Total'])
with pd.ExcelWriter('expenses.xlsx', engine='openpyxl') as writer:
    df_expenses.to_excel(writer, sheet_name='expenses', index=False)
    df_totals.to_excel(writer, sheet_name='total', index=False)
print("Expenses and category totals written to 'expenses.xlsx'.")
    