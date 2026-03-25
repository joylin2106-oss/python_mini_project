sum = 0
while True:
   print("1.games")
   print("2.utilities")
   print("3.Exit")
   choices = int(input("Enter a number: "))
 
   if choices== 1:
        print("game")
        print("Welcome to Games section")
        
        while True:
            print("1.Guessing game ")
            print("2.back ")
            user_value = int(input("Enter a number: "))
            if user_value == 1:
             print("Guessing game")
            else: 
             print("Go Back")  
             break   
   elif choices==2:
     print("utilities")
     print("Welcome to utilities section")
     while True:
        print("1.Even/Odd")
        print("2.Sum of number")
        print("3.Go back")
        user_inpt2 = int(input("Enter a Number: "))
        if user_inpt2 == 1:
           num = int(input("Enter any desire number: "))
           print("")
           if num % 2 ==0:
              print("EVEN")
           else: 
              print("ODD")  
     
        elif user_inpt2 == 2:
          sum = 0
          while True:
             user = int(input("Enter number: "))
             if user < 0:
               print("Stop ")
               break
             else:
              sum = sum + user
              print(sum)
          print("Total:", sum)     
                  
        
        elif user_inpt2 == 3:
           print("Go Back")
           break
            
        
   elif choices == 3:
     print("Exit") 
     break  
   else:
        print("Invalid")     





