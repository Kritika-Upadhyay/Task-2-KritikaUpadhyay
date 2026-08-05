def Expense_Tracker():

    print("-"*7,"MY EXPENSES","-"*7)

    print("1. Add Expenses \n2. View Expenses \n3. Search Expenses \n4. Edit Expense \n5. Delete Expense \n6. View Total Expenses \n7. Exit")
    print("-"*28)

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

            for category, amount in expense.items():
                f.write(f"{category}: Rs. {amount}\n")

            f.write("\n")

        print("="*30)
        print(expense)
        print("="*30)

    elif(choice == 2):
        with open("Expense.txt") as f:
            r = f.read()
            print("="*30)
            print(r)
            print("="*30)

    elif(choice == 3):
        print("-"*30)
        print("1. Search by Date \n2. Search by Category")
        print("-"*30)

        sub_choice = int(input("Enter your choice: "))

        if(sub_choice == 1):
            search_date = input("Enter the date (DD/MM/YYYY): ")

            found = False

            with open("Expense.txt") as f:
                for line in f:
                    if line.strip() == search_date:
                        found = True
                        print("="*30)
                        print(line, end="")
                        print("="*30)
                        continue

                    if found:
                        if line.strip() == "":
                            print("="*30)
                            break

                        print(line, end="")

            if not found:
                print("-"*7,"Error: Date not Found!","-"*7)

        if(sub_choice == 2):
            search_category = input("Enter the category: ")
            current_date = ""

            found = False 

            with open("Expense.txt") as f:
                for line in f:
                    if len(line.strip()) == 10 and "/" in line:
                        current_date = line.strip()

                    if line.lower().startswith(search_category.lower() + ":"):
                        found = True 
                        print("="*30)
                        print(current_date)
                        print(line)
                        print("="*30)
                        continue

            if not found:
                print("-"*7,"Error: Category not Found!","-"*7)

    elif(choice == 4):
        edit_date = input("Enter the date in which you want to make changes (DD/MM/YYYY): ")
        edit_category = input("Enter the category in which you want to make changes: ")

        found_date = False
        found_category = False

        with open("Expense.txt") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if lines[i].strip() == edit_date:
                    found_date = True 
                    continue 

                if found_date:
                    if lines[i].lower().startswith(edit_category.lower() + ":"):
                        found_category = True 

                        new_category = input("Enter the new category (eg: Food, Shopping, Insurance, etc.): ")
                        new_amount = int(input("Enter the total amount spent on that category: "))
                        
                        lines[i] = f"{new_category}: Rs. {new_amount}\n"

                    if lines[i].strip() == "":
                        break

            if found_category:
                with open("Expense.txt", "w") as f:
                    f.writelines(lines)

                print("-"*30)
                print("Expense Updated Successfully!")
                print("-"*30)


            else:
                print("-"*7,"Error: Expense not Found!","-"*7)

    elif(choice == 5):
        delete_date = input("Enter the date in which you want to Delete an expense (DD/MM/YYYY): ")
        delete_category = input("Enter the category which you want to Delete: ")
        
        found_date = False
        found_category = False
        
        with open("Expense.txt") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if lines[i].strip() == delete_date:
                    found_date = True 
                    continue 
        
                if found_date:
                    if lines[i].lower().startswith(delete_category.lower() + ":"):
                        found_category = True 
                                
                        del lines[i]
                        break
        
                    if lines[i].strip() == "":
                        break
        
            if found_category:
                with open("Expense.txt", "w") as f:
                    f.writelines(lines)
        
                print("-"*30)
                print("Expense Deleted Successfully!")
                print("-"*30)
        
        
            else:
                print("-"*7,"Error: Expense not Found!","-"*7)

    elif(choice == 6):


Expense_Tracker()