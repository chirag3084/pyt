number1 = int(input("what is your first number : "))

number2 = int(input("what is your second number : "))


print(" enter your  operator (+,-,*,% )")      

operator = input("enter your operator :" )

if operator == "+":
	print(number1 + number2)

elif operator == "-":
	print(number1 - number2)

elif operator == "*":
	print(number1 * number2)


elif operator == "/":
	print(number1 / number2)

else :

    print("invalid operation ")
