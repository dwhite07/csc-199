#Starting a while loop. Will repeat until proven false.
while True:

        #Printing the menu options
        print("1. Enter a String")
        print("2. See Your String")
        print("3. See Your String 3 Times")

        #Allowing the user to input a value for the variable "selected"
        selected=int(input("Enter Choice: "))

        #This step will only activate if user chooses option 1 in menu
        #If activated, the step will allow the user to enter their own string
        if (selected == 1):
            user_string = input("Enter A String: ")

        #This step will only activate if user chooses option 2 in menu
        #If activated, the step will display the user's string to them
        elif (selected == 2):
                print(user_string)

        #This step will only activate if user chooses option 3 in menu
        #If activated, the step will display the user's string to them 3 times
        elif (selected == 3):
                print(user_string)
                print(user_string)
                print(user_string)

        #This step will only activate if user chooses option 4 in menu
        #If activated, the step will exit the program
        elif (selected == 4):
                print('Exiting')
                break
                


