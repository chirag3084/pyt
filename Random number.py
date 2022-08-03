import random

user_number = input("enter a number : ")

if user_number.isdigit():
	user_number = int(user_number)
	
	if user_number <= 0:
		print("please enter number greater than 0")
		quit()
else:
	        print("please enter proper number")
	        quit()

random_number= random.randint(0, user_number)
guesses = 0

while True:
	guesses += 1
	user_guess = input("make a guess : ")
	if user_guess.isdigit():
		user_guess = int(user_guess)
	else:
		print("enter a proper number")
		continue
		
	if user_guess == random_number:
		print("you got it! ")
		break
	elif user_guess > random_number:
		print("your number is big ")
	else:
		print("your number is small")
		
print("you got it in",guesses,"guesses")

