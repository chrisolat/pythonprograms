import random 
import os
count = 1
	
	

	
	

def start():
	rand = random.randint(1,100)
	global count
	game_on = True
	while(game_on):
		guess = int(input("guess a number\n"))
		if count == 10:
			print("time up!. The number is ", rand)
			break
		if guess == rand:
			print("you guessed right\n")
			print("you tried ", count, " times")
			game_on = False
		elif guess > rand:
			print("too high, try again\n")
		elif guess < rand:
			print("too low, try again\n")
		
		
		count += 1

	ans = input("do you want to play again?(y/n)\n")
	if(ans == 'y' or 'Y'):
		game_complete()
	elif(ans == 'n' or 'N'):
		exit()
	else:
		print("input y or n")
	
	
def game_complete():
	global count
	count = 1
	start()
	
start()