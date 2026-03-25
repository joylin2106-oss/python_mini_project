password =21006
chances = 0
while chances<3:
    user_value =int(input("Enter password: "))
    if user_value == password:
        print(" Correct Password, Access Granted!")
        break
    else:
        print("Wrong Password,  Try Again Later!")
        chances+=1
        if chances<3:
                print("Hint = date")
        
if chances == 3:
    print("Blocked")
print()