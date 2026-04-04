date = input("Enter the date: ")
item = input("Enter the item: ")
amount = int(input("Enter the amount: "))


food_exp = {
    "date":date,
    "item" : item,
    "amount" :amount
}

print(food_exp["date"])
print(food_exp["item"])
print(food_exp["amount"])


date = input("Enter the date: ")
item = input("Enter the item: ")
amount = int(input("Enter the amount: "))

food_exp1={
    "date":date,
    "item" : item,
    "amount" :amount
}

print(food_exp1["date"])
print(food_exp1["item"])
print(food_exp1["amount"])

exp_store =[]
exp_store.append(food_exp)
exp_store.append(food_exp1)

print(exp_store)




