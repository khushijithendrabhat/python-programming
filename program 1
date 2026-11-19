text = input("Enter the amount: ")

if not text.isdigit():
    print("Please enter a valid positive amount!")
else:
    amount = int(text)

    notes = [100, 50, 10]

    for n in notes:
        count = amount // n
        amount = amount % n

        print(n, "rupee note(s):", count)
