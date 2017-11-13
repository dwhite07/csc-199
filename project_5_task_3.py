#Starting a conditional loop+printing the menu
print("Welcome to the cash register. Please note that your balance is currently $0 so you can't make a withdrawl until a deposit is made")
while True:
    print("1. put money into the cash register: ")
    print("2. withdrawl money from the cash register: ")
    print("3. make change: ")
    print("4. balance check: ")
    print("5. quit ")

    #Setting user selected variable
    selected = int(input("Enter Choice: "))
    
    #First option on menu will activate this step
    if (selected == 1):

        #Setting Variables
        balance = 0
        choice_1 = 0
        choice_2 = 0
        choice_3 = 0
        choice_4 = 0
        choice_5 = 0
        choice_6 = 0

        #User inputs amount of $1 bills to deposit and it gets added to their balance
        choice_1 = int(input("Insert how many $1 bills: "))
        choice_1 = choice_1 * 1
        balance += choice_1

        #User inputs amount of $5 bills to deposit and it gets added to their balance
        choice_2 = int(input("Insert how many $5 bills: "))
        choice_2 = choice_2 * 5
        balance += choice_2

        #User inputs amount of $10 bills to deposit and it gets added to their balance
        choice_3 = int(input("Insert how many $10 bills: "))
        choice_3 = choice_3 * 10
        balance += choice_3

        #User inputs amount of $20 bills to deposit and it gets added to their balance
        choice_4 = int(input("Insert how many $20 bills: "))
        choice_4 = choice_4 * 20
        balance += choice_4

        #User inputs amount of $50 bills to deposit and it gets added to their balance
        choice_5 = int(input("Insert how many $50 bills: "))
        choice_5 = choice_5 * 50
        balance += choice_5

        #User inputs amount of $100 bills to deposit and it gets added to their balance
        choice_6 = int(input("Insert how many $100 bills: "))
        choice_6 = choice_6 * 100
        balance += choice_6
        
    #Second option on menu will activate this step
    if (selected == 2):

        #Setting Variables
        option_1 = 0
        option_2 = 0
        option_3 = 0
        option_4 = 0
        option_5 = 0
        option_6 = 0
        
        #User inputs amount of $1 bills to withdrawl and it gets subtracted from their balance
        option_1 = int(input("Withdrawl how many $1 bills: "))
        option_1 = option_1 * 1
        if (balance < option_1):
            print("Not enough money to withdrawl")
        if (balance >= option_1):
            balance -= option_1

        #User inputs amount of $5 bills to withdrawl and it gets subtracted from their balance
        option_2 = int(input("Withdrawl how many $5 bills: "))
        option_2 = option_2 * 5
        if (balance < option_2):
            print("Not enough money to withdrawl")
        if (balance >= option_2):
            balance -= option_2

        #User inputs amount of $10 bills to withdrawl and it gets subtracted from their balance
        option_3 = int(input("Withdrawl how many $10 bills: "))
        option_3 = option_3 * 10
        if (balance < option_3):
            print("Not enough money to withdrawl")
        if (balance >= option_3):
            balance -= option_3

        #User inputs amount of $20 bills to withdrawl and it gets subtracted from their balance
        option_4 = int(input("Withdrawl how many $20 bills: "))
        option_4 = option_4 * 20
        if (balance < option_4):
            print("Not enough money to withdrawl")
        if (balance >= option_4):
            balance -= option_4

        #User inputs amount of $50 bills to withdrawl and it gets subtracted from their balance
        option_5 = int(input("Withdrawl how many $50 bills: "))
        option_5 = option_5 * 50
        if (balance < option_5):
            print("Not enough money to withdrawl")
        if (balance >= option_5):
            balance -= option_5

        #User inputs amount of $100 bills to withdrawl and it gets subtracted from their balance
        option_6 = int(input("Withdrawl how many $100 bills: "))
        option_6 = option_6 * 100
        if (balance < option_6):
            print("Not enough money to withdrawl")
        if (balance >= option_6):
            balance -= option_6

    #Third option on menu will activate this step
    if (selected == 3):

        #Allowing user to input cost of product+the amount of money they wish to receive change for
        cost = int(input("What is the price of the item being purchased: "))
        money = int(input("Insert amount of money to make change for: "))
        change = money - cost

        #Setting Variables
        change1 = 0
        change2 = 0
        change3 = 0
        change4 = 0
        change5 = 0
        change6 = 0

        #Determining how many $100 bills are received as change+subtracting that from total change variable
        onehundred = int(change / 100)
        change1 += onehundred
        change -= onehundred * 100

        #Determining how many $50 bills are received as change+subtracting that from total change variable
        fifty = int(change / 50)
        change2 += fifty
        change -= fifty * 50

        #Determining how many $20 bills are received as change+subtracting that from total change variable
        twenty = int(change / 20)
        change3 += twenty
        change -= twenty * 20

        #Determining how many $10 bills are received as change+subtracting that from total change variable
        ten = int(change / 10)
        change4 += ten
        change -= ten * 10

        #Determining how many $5 bills are received as change+subtracting that from total change variable
        five = int(change / 5)
        change5 += five
        change -= five * 5

        #Determining how many $1 bills are received as change+subtracting that from total change variable
        one = int(change / 1)
        change6 += one
        change -= one * 1

        #Showing the amount of change given with every bill
        print("Your change is this many $100 bills: ", onehundred)
        print("Your change is this many $50 bills: ", fifty)
        print("Your change is this many $20 bills: ", twenty)
        print("Your change is this many $10 bills: ", ten)
        print("Your change is this many $5 bills: ", five)
        print("Your change is this many $1 bills: ", one)

    #Fourth option on menu will activate this step
    if (selected == 4):

        #Setting a variable equal to the balance so the balance can remain the same
        bills = balance

        #Determining the number of $100 bills in balance+subtracting that from total amount
        a = int(bills / 100)
        a2 = a * 100
        bills -= a2

        #Determining the number of $50 bills in balance+subtracting that from total amount
        b = int(bills / 50)
        b2 = b * 50
        bills -= b2

        #Determining the number of $20 bills in balance+subtracting that from total amount
        c = int(bills / 20)
        c2 = c * 20
        bills -= c2

        #Determining the number of $10 bills in balance+subtracting that from total amount
        d = int(bills / 10)
        d2 = d * 10
        bills -= d2

        #Determining the number of $5 bills in balance+subtracting that from total amount
        e = int(bills / 5)
        e2 = e * 5
        bills -= e2

        #Determining the number of $1 bills in balance+subtracting that from total amount
        f = int(bills / 1)
        f2 = f * 1
        bills -= f2

        #Displaying the balance and the amount of bills of each type
        print("Your current balance is: ", balance)
        print("You have this many $100 bills: ", a)
        print("You have this many $50 bills: ", b)
        print("You have this many $20 bills: ", c)
        print("You have this many $10 bills: ", d)
        print("You have this many $5 bills: ", e)
        print("You have this many $1 bills: ", f)

    #Fifth option on menu will activate this step
    if (selected == 5):
        print("Thanks for shopping!")
        break

    #If an option greater than 5 on the menu is selected a message will appear
    if (selected > 5):
        print("Your choice is out of range. Please enter a selection in the appropriate range: ")

    #If an option less than 1 on the menu is selected a message will appear
    if (selected < 1):
        print("Your choice is out of range. Please enter a selection in the appropriate range: ")
