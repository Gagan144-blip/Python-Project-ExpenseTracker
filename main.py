
expensesList =[] #list of all expenses in form of dictionary

print("Welcome To Expense Tracker:karcha kam kiya karo")

while True:
    print("*****Menu******")
    print("****************")
    print("1.Add expense")
    print("2.View Expenses")
    print("3.View Total Expenses")
    print("4.Exit")

    choice = int(input("Please Enter your Choice: "))

    if(choice==1):
        date = input("Enter Date for Expenses: ")
        Category = input("Enter the Category(e.g:food,cloths,Books etc.): ")
        Description = input("Add Short Discription for Expenses: ")
        Amount = float(input("Enter the Amount: "))

        expense = {
            "Date":date,
            "Category":Category,
            "Description":Description,
            "Amount":Amount
        }

        expensesList.append(expense)
        print("\n DONE Bro!! Expenses added Successfully")

    #2.VIEW ALL EXPENSES
    elif(choice==2):
        if(len(expensesList)==0):
            print("\n No Expenses to Show!!")
        else:
            print("\n Your Expenses: ")
            count = 1
            for item in expensesList:
                print(f"\nExpense No. {count} -> {item["Date"]}, {item["Category"]}, {item["Description"]}, {item["Amount"]}")
                count +=1
#3. VIEW TOTAL SPENDINGS
    elif(choice==3):
        total = 0
        for eachItem in expensesList:
            total = total + eachItem['Amount']
        
        print("Total Expenses: ", total)
#4. Exit
    elif(choice==4):
        print("Thank You for using Expense Tracker!!")
        break
    else:
        print("Invalid Choice!! Please Try Again")
                



