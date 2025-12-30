import random
while True:
    option=input("enter rock paper or scissor")
    p=["rock","paper","scissor"]
    c=random.choice(p)
    if option==c:
        print("tie")
    elif option=="rock":
        if c=="scissor":
            print("you win, rock smashes scissors")
        else:
            print("you loose")
        
    if option==c:
        print("tie")
    elif option=="paper":
        if c=="rock":
            print("you win, paper covers rock")
        else:
            print("you loose")
            if option==c:
                print("tie")
    elif option=="paper":
        if c=="rock":
            print("you win, papers covers rock")
        else:
            print("you loose")
        