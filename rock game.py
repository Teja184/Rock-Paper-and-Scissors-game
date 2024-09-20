import random
def game(): 
    user=input("enter rock or paper or scissor : ")
    ch=["rock","paper","scissor"]
    comp=random.choice(ch) 
    print("user choice : ",user)
    print("computer choice : ",comp)  
    if(user==comp):
        print("It's a tie")
    elif(user=="rock" and comp=="paper"):
        print("Lose")
    elif(user=="rock" and comp=="scissor"):
        print("Win")
    elif(user=="paper" and comp=="rock"):
        print("Win")
    elif(user=="paper" and comp=="scissor"):
        print("Lose")
    elif(user=="scissor" and comp=="rock"):
        print("Lose")
    elif(user=="scissor" and comp=="paper"):
        print("Win")
    a=input("If you want to play type yes other wise no : ")
    if a=="yes":
        game()
    elif a=="no":
        print("game end")
game()


