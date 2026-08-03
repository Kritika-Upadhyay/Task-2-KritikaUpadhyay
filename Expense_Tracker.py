def Expense_Tracker():

    print("-"*7,"MY EXPENSES","-"*7)

    print("1. Add Expenses \n2. View Expenses \n3. Search Expenses \n4. Edit Expense \n5. Delete Expense \n6. View Total Expenses \n7. Exit")

    expense = {}
    choice = int(input("Enter your choice (1-7): "))

    if(choice == 1):
        no_expense = int(input("Enter the number of expenses you want to add: "))
        date = input("Enter the date of expenses (DD/MM/YYYY): ")

        for i in range (1, no_expense + 1):

            category = input("Enter the category of your expense (eg: Food, Shopping, Insurance, etc.): ")
            amount = int(input("Enter the total amount spent on that category: "))

            expense.update({category: amount})

        with open("Expense.txt", "a") as f:
            f.write(date + "\n")
            f.write("\n")

            for category, amount in expense.items():
                f.write(f"{category}: Rs. {amount}\n")

            f.write("\n"*2)

        print("-"*30)
        print(expense)
        print("-"*30)

    elif(choice == 2):
        with open("Expense.txt") as f:
            r = f.read()
            print("="*30)
            print(r)
            print("="*30)

Expense_Tracker()