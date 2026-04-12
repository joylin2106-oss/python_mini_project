def food_expense_tracker():
        print("----Food expense tracker----")
        same_date = input("Are all products from same day(yes/no): ")
        if same_date == "yes":
           date = input("Enter the date: ")
        exp_store =[]
        exp_total = 0 
        n = int(input("Enter number: "))
        for i in range (1,n+1):
            if same_date != "yes":
                date = input("Enter the date: ")
            item = input("Enter the item name: ")
            amount = int(input("Enter the amount: "))
            food_exp = {
                "date":date,
                 "item" : item,
                 "amount" :amount
            }
            exp_total += food_exp["amount"]
            exp_store.append(food_exp)
            print(exp_store)
            for exp in exp_store:
                print(exp["date"],exp["item"],exp["amount"])
            print("total Amount: ",exp_total)
            return exp_store,exp_total
def usage_tracker():
    item_total = 0 
    print("---usage tracker---")
    from datetime import datetime, date
    from datetime import timedelta
    essential_list = []
    m = int(input("Enter a number: "))
    for i in range(1,m+1):
        items = input("Enter the item name: ")
        item_amount = int(input("Enter the amount: "))
        date_opened = input("Enter opened date(YY-MM-DD): ")
        converted = datetime.strptime(date_opened,"%Y-%m-%d")
        current_month = converted.month 
        current_year= converted.year
        current_day = converted.day
        duration = input("Enter the duration: ").lower().split()     # split () - split the string 
        number = int(duration[0])
        duration_type = duration[1]
        if duration_type == "days" or type == "day":
            end_date = converted + timedelta(days = number)
        elif duration_type == "months" or type == "month":
            new_month =  current_month + number  
            if new_month >12:
               new_month -=  12
               current_year += 1  # to stop the error
            end_date = datetime(current_year,new_month,current_day)
        else:
            print("Invalid")
        today = date.today()
        if today < end_date.date():
            print("Safe to use!", today-end_date.date())
        elif today == end_date.date():
            print("Last day to use!")
        else:
            print("Already Expired!")    
        
        usage_store ={
           "items": items,
           "item_amount": item_amount,
           "date_opened": date_opened,
           "duration": duration, 
           "end_date": end_date
         }
        item_total += item_amount
        essential_list.append(usage_store)
        print("total spent :",item_total)
        print(essential_list,item_total)
        return essential_list,item_total

def discretionary_tracker():
    print("---discretionary tracker----")
    from datetime import datetime 
    disc_store = []
    disc_total = 0 
    n = int(input("enter the number of items: "))
    for i in range(1,n+1):
        disc_date = input("Enter the date(yy-mm-dd):")
        converted_disc = datetime.strptime(disc_date,"%Y-%m-%d")    # striptime - convert the string into date so that we can add the date 
        disc_name = input("Enter the name: ")
        disc_amount = int(input("Enter the amount: "))
        disc_usage = {
             "disc_date": disc_date,
              "disc_name": disc_name,
              "disc_amount" : disc_amount
            }
        disc_total+= disc_amount
        disc_store.append(disc_usage)
        print(disc_store)
        print("Total spent: ",disc_total)
        return disc_total,disc_store

#----- budget -------

def saving_tracker(exp_total,disc_total,item_total):
    budget =int(input("Enter your budget(income/pocket money): "))
    saving_goal = int(input('Enter your saving goal: '))
    total_spent = exp_total + disc_total + item_total
    saving = budget - total_spent
    saving_tracker = {
      "total_spent": total_spent,
      "budget" : budget,
      "saving_goal" : saving_goal,
      "saving":saving
    
    }
    print("total spent: ",total_spent)
    print("savings: ",saving)

#----- savings ------

    if saving == saving_goal:
        print("You Achieved it!")
    elif saving > saving_goal:
        print("Amazing you saved more than your goal!", saving - saving_goal)
    else:
        print("Nxt time you can Achieve! you need: ", saving_goal - saving) 
    
     # this helps in dopamine release and motivates to save nxt time 
   
    return()

def menu():
  exp_total = 0 
  disc_total = 0 
  item_total = 0
  exp_store =[]
  essential_list=[]
  disc_store = []
  while True:
    print("MENU")
    print("1.Food expense tracker")
    print("2.Usage tracker")
    print("3.Discretionary tracker")
    print("4.Saving tracker")
    print("5.Exit")

    choice = int(input("Enter the menu number: "))
    if choice == 1:
        exp_store, exp_total =food_expense_tracker()
    elif choice == 2:
        essential_list,item_total = usage_tracker()
    elif choice == 3:
        disc_total,disc_store = discretionary_tracker()
    elif choice == 4:
        saving_tracker(exp_total,disc_total,item_total)
    elif choice == 5:
        print("Goodbye")
        break
    else:
         print("Invalid") 
menu()
