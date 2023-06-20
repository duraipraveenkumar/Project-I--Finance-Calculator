#!/usr/bin/env python3
import math

# This line of code is printing a message to the user, prompting them to select an option between
# Investment and Bond. It also provides a brief description of what each option does.
print("Select an option from\nInvestment - to calculate the amount of interest you'll earn on your investment \nBond - to calculate the amount you'll have to pay on a home loan")

# This line of code is prompting the user to enter either 'investment' or 'bond' and storing the
# user's input in the variable `calculator_choice`. The `.lower()` method is used to convert the
# user's input to lowercase letters, which allows for case-insensitive comparison later in the code.
calculator_choice = input("Enter either 'investment' or 'bond': ").lower()

# This code block is executed if the user selects 'investment' as their calculator choice. It prompts
# the user to enter the deposit amount, interest rate, duration of investment, and whether they want
# simple or compound interest. It then calculates the total amount after the specified duration using
# the appropriate interest calculation formula and prints the result to the user. If the user enters
# an invalid calculator choice, the code prints a message asking them to try again.
if (calculator_choice != 'investment') and (calculator_choice != 'bond') :
	print('please try again')
elif calculator_choice == 'investment' :
	deposit = float(input("Enter the deposit amount: "))
	interest_rate = float(input("Enter the interest rate: "))
	duration = int(input("Enter the number of years you would like to invest for: "))
	interest = input("Do you want 'simple' or 'compound': ").lower()
	if interest == 'simple' :
		r = (interest_rate/100)
		P = deposit
		t = duration
		A =P *(1 + r*t)
	elif interest == 'compound' :
		P = deposit
		t = duration
		r = (interest_rate/100)
		A = P * math.pow((1+r), t)
	print("The total amount after", duration, " years is" , round(A ,2))
# This code block is executed if the user selects 'bond' as their calculator choice. It prompts the
# user to enter the value of the house, the interest rate, and the number of months they would like to
# repay the bond. It then calculates the monthly repayment amount using the appropriate formula and
# prints the result to the user.
elif calculator_choice == 'bond' :
	value = float(input("Enter the value of the house: "))
	interest_bond = int(input("Enter the interest rate: "))
	time = int(input("Enter the number of months you would like to repay the bond: "))
	P = value
	i = (interest_bond/100)/12 
	n = time
	repayment = (i * P) / (1 - (1 + i) ** (-n))
	print("The monthly repayment is", round(repayment, 2))
