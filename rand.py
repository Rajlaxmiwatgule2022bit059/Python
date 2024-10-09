import random

def random_number():    
	return random.randint(0, 20) 
def logic(y,num):
	if y == num:  
			print("You guessed it right!")
			return True
	else:
			print(f"Wrong!")
			return False  
			
def hint(num,y):
	if num < y:
		print(f"the number is greater than {num}")
	elif num >y:
		print(f"the number is lesser than {num}")

def guess_the_number():
	y = random_number() 
	if y <= 10 :
		print("Guess the number between 0 to 10 ") 
		
	else:
		print("Guess the number between 11 to 20 ")
	while True :
		 
		num = int(input())
		hint(num,y) 
		if logic(y,num):
			break
	
print(guess_the_number())
