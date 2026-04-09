print("----Food expense tracker----")
exp_store =[]
exp_total = 0 
n = int(input("Enter number: "))
for i in range (1,n+1):
    
    date = input("Enter the date: ")
    item = input("Enter the item: ")
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

#----usage_tracker-----
print("---usage tracker---")
from datetime import datetime 
from datetime import timedelta
essential_list = []
m = int(input("Enter a number: "))
for i in range(1,m+1):
    items = input("Enter the item name: ")
    date_opened = input("Enter date (YY-MM-DD): ")
    converted = datetime.strptime(date_opened,"%Y-%m-%d")
    current_month = converted.month 
    current_year= converted.year
    current_day = converted.day



    duration = input("Enter the duration: ").lower().split()
    number = int(duration[0])
    type = duration[1]
    
    
    if type == "days" or type == "day":
        end_date = converted + timedelta(days = number)
    elif type == "months" or type == "month":
        
        new_month =  current_month + number  
        if new_month >12:
            new_month -=  12
            current_year += 1  # to stop the error
        end_date = datetime(current_year,new_month,current_day)

    else:
        print("Inavlid")
    
    usage_tracker ={
        "items": items,
        "date_opened": date_opened,
        "duration": duration, 
        "end_date": end_date
        }
    essential_list.append(usage_tracker)

print(essential_list)

# ---- discretionary-----
print("---discretionary tracker----")
disc_store = []
disc_total = 0 
n = int(input("enter the number of items: "))
for i in range(1,n+1):
    disc_date = input("Enter the date(yy-mm-dd):")
    converted_disc = datetime.strptime(disc_date,"%Y-%m-%d")

    disc_name = input("Enter the name: ")
    disc_amount = int(input("Enter the amount: "))
    disc_exp = {
        "disc_date": disc_date,
        "disc_name": disc_name,
        "disc_amount" : disc_amount
    }
    disc_total+= disc_amount
    disc_store.append(disc_exp)
print(disc_store)
print("Total spent: ",disc_total)


budget =int(input("Enter your budget(income/pocket money): "))
saving_goal = int(input('Enter your saving goal: '))

total_spent = exp_total + disc_total 
saving = budget - total_spent

saving_tracker = {
    "total_spent": total_spent,
    "budget" : budget,
    "saving_goal" : saving_goal,
    "saving":saving
    
}
print(total_spent)
print(saving)

if saving == saving_goal:
    print("You Achieved it!")
elif saving > saving_goal:
    print("Amazing you saved more then your goal", saving - saving_goal)
else:
    print("Nxt time you can Achieve! you need: ", saving_goal - saving) 
    
     # this helps in dopamine release and motivates to save nxt time 







tracker = {
    "expenses" : exp_store ,
    "essentials": essential_list,
    "discretionary":disc_store,
    "savings": saving_tracker
}
print(tracker)
    