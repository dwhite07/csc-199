while True:

        print("1. Enter a String")
        print("2. See Your String")
        print("3. See Your String 3 Times")

        selected=int(input("Enter Choice: "))

        if (selected == 1):
            user_string = input("Enter A String: ")             
             
        elif (selected == 2):
                print(user_string)

        elif (selected == 3):
                print(user_string)
                print(user_string)
                print(user_string)
        elif (selected == 4):
                print('Exiting')
                break
                


