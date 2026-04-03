# ----------------
#     MAIN MENU
#------------------
import random 

def guess_game():
    chances = 0 
    rand_num = random.randint(1,50)
    while chances<=10:
         user_value1= int(input("Enter a number:" ))
         if user_value1 == rand_num :
            print("Guessed correctly:",user_value1)
            chances+=1
            break
         elif user_value1>=rand_num:
            print("Higher number")
         else:
            print("Lower number") 
        
def odd_even(num):
   
   if num % 2 ==0:
     print("EVEN")
   else: 
      print("ODD")
   print(num)
   return num

def sum_num():
  sum = 0
  count = 0 
  while count<=10:
   user = int(input("Enter number: "))
   if user < 0:
    print("Stop ")
    
   else:
    sum = sum + user
    print(sum)
    count+=1  
    print("Total:", sum)
  
 

while True:
   print("1.games")
   print("2.utilities")
   print("3.Exit")
   choices = int(input("Enter a number: "))

# ----------- GAMES MENU --------------
  
   if choices== 1:
        print("-----game-----")
        print("Welcome to Games section")

#------------ GUESSING GAME -----------     
 
        while True:
            print("1.Guessing game")
            print("2.back ")
            user_value = int(input("Enter a number: "))
            if user_value == 1:
             print("----Guessing game----")
             guess_game()
            else: 
             print("Go Back")  
             break   

# ---------- UTILITIES MENU ------------
   
   elif choices==2:
     print("-----utilities-----")
     print("Welcome to utilities section")
     while True:

# --------- ODD/EVEN -------------
       
        print("1.Even/Odd")
        print("2.Sum of number")
        print("3.Go back")
        
        user_inpt1 = int(input("Enter a Number: "))
        
        if user_inpt1 == 1:
           print("-----EVEN/ODD-----")
           num = int(input("Enter any desire number: "))
           odd_even(num)

# ---------- SUM - NUMBER --------------
        elif user_inpt1 == 2:
          print("-----sum of number-----")
          sum_num()     
        elif user_inpt1 == 3:
           print("Go Back")
           break
        else:
           print("Invalid")
            
        
   elif choices == 3:
     print("Exit") 
     break  
   else:
        print("Invalid")     





