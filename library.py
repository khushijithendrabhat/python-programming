
days = int(input("Enter the number of days late: "))

if days <= 5:
    print("Fine = Rs. 0.50")
elif days <= 10:
    print("Fine = Rs. 1")
elif days <= 30:
    print("Fine = Rs. 5")
else:
    print("Membership cancelled")