import random
secret_number = random.randint(1,10)
attempts =3
while attempts >0:
    guess =int(input("guess the number(between 1 and 10):"))
    if guess < 1 or guess >10:
       print("your guess is out of range. please guess a number")
       continue
    if guess == secret_number:
       print("congratulation! you guessed the correct number.") 
       break
    elif guess > secret_number:
         print("too high.try again.")
         attempts -= 1
    else:
        print("too low.try again.")
        attempts -= 1
else:
    print(f"better luck next time! the secret number was{secret_number}")
    