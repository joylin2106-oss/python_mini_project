import random
won = False
low = 1
high = 100 
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
        print(" Too low \n Guess between ")
    else:
        print("high range:choose lower number")
if not won:
    print("better luck next time")
    print("Correct number: ",num)

print()    


   