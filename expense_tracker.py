
exp_store =[]
total = 0 
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
  
    total += food_exp["amount"]
        
    exp_store.append(food_exp)
   
print(exp_store)
for exp in exp_store:
    print(exp["date"],exp["item"],exp["amount"])
print("total Amount: ",total)

#----usage_tracker-----
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




    