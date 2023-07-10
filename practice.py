import random
num = random.randint(0,10)
guess = int(input("Please enter a number between 0 to 10:"))
while num!=guess:
    
    if guess < num:
        print("TOO LOW!")
        guess = int(input("Please enter a number between 0 to 10:"))
    elif guess>num:
        print("TOO HIGH")  
        guess = int(input("Please enter a number between 0 to 10:"))
    else:
        break
print("You Guessed it right!")
print(f'computer chose {num}')
        
