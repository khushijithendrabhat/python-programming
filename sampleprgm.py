amount = int(input("enter the amount to withdraw:"))
if amount<0:
    print("invalid amount")
n100 = amount // 100
amount = amount % 100
n50 = amount // 50
amount = amount % 50
n10 = amount // 10
print(" number of 100 rupee notes:",n100)
print("number of 50 rupee notes:",n50)
print("number of 10 rupee notes:",n10)


