import random
play=True
n=str(random.randint(10,20))
print("Guess a number between 10 and 20")
while play:
    guess=input("Give me best guess")
    if n==guess:
        print("You win")
        print("number is ",n)
        break
    else:
        print("try again")