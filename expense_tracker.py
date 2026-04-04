
exp_store =[]
expenses = 0 
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
    exp_store.append(food_exp)
print(exp_store)
for exp in exp_store:
    print(exp["date"],exp["item"],exp["amount"])



