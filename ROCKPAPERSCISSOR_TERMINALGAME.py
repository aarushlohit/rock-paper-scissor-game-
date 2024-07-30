import random as r
print('''ROCK PAPER SCISSOR''')
a = "GameMenu"
b = a.center(len(a) + 100, "=")
print(b)
Playername= input("Enter your name:")
Playerchoice= input("Enter... \n 1) rock 🪨 \n 2) paper🧻 \n 3) scissor ✂️ \n \n choose:")
probab=["rock","paper","scissor"]
computerchoice= r.choice(probab)
try:
    if Playerchoice == "paper" and computerchoice == "rock":
        print("Playerchoice =", Playerchoice)
        print(Playername , "🥳 wins")
    elif Playerchoice == "scissor" and computerchoice == "paper":
        print("Playerchoice =", Playerchoice)
        print(Playername , "🥳 wins")
    elif Playerchoice == "scissor" and computerchoice == "paper":
            print("Playerchoice =", Playerchoice)
            print(Playername ,"🥳 wins")
    else:
     print("computerchoice 🤖 =",computerchoice)
     print("😎Python wins Better luck next time")
except:
    print("please enter correct input Mr.🥸"+Playername)
finally:
    print("Game finished have a nice day😉!"+ Playername)
   



