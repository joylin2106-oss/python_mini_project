import random
won = False
guess = 0
chances = 0 
num = random.randint(1,100)
while chances< 3:
    guess = int(input("Enter a number: "))
    chances+=1
    if guess == num:
        print("Guessed correctly")
        won = True
        break
    elif guess <num:
        print("low range:choose higher number")
    else:
        print("high range:choose lower number")
if not won:
    print("better luck next time")
    print("Correct number: ",num)

print()    


   