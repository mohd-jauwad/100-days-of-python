#This program splits the bill between the specified number of people.
print("Welcome to the tip calculator ")
totalBill = float(input("What's the total bill \n->"))
print("Sweet ! Now, ")
tip = float(input("What percentage tip would you like to give ? 10, 12 or 15 \n->"))
print("Very Generous of you :) ")
splitBill = int(input("How many to split the bill between ?\n-> "))
print("Impressive, Very Nice. (Patrick Bateman reference)")
tippedBill = int(tip / 100 * totalBill + totalBill)
div_tippedBill = (tippedBill /splitBill)
print("Each person should pay " ,div_tippedBill)
