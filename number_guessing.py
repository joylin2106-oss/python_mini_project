import random
guess = 0
won = False
num = random.randint(1,100)


attempts = 0
while attempts<=10:
    guess= int(input("guess: "))
    attempts+=1
    if guess == num:
            won = True
            print("guessed correctly")
            print(f"you guesses in: {attempts}")
            break
    elif guess <num:
          print("low range")
     
    else:
          print("higher range")
      
if not won:      
      print("better luck next time") 
print()  

        