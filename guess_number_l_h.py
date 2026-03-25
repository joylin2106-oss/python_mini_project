import random 
guess = 0
low = 1
high = 100
chances = 0
num = random.randint(1,100)
while chances<=5:
    guess = int(input("Enter a number: "))
    print(f"Guess between {low} and {high}")
    chances+=1
    if guess == num:
        print("Guesses correctly")
        print("you guessesd it in {chances} attempts")
        break
    elif guess <num:
        print("Too low")
        low = guess + 1 
    elif guess>num:
        print("Too high")
        high = guess - 1
    else: 
        print(" you lost")    
print()            
print("DEBUG:",low,high)