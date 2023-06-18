# TIP CALCULATOR

print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
pp_to_split = int(input("How meny people to split the bill? "))

total_percentage = (total_bill * percentage) / 100
total_amount = (total_bill + total_percentage) / pp_to_split

# total = round(total_amount, 2)
total = "{:.2f}".format(total_amount)

print(f"Each person should pay: ${total}")
