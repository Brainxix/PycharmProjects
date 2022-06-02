import random
while True:
 choices = ["rock", "paper", "scissors"]
 computer = random.choice(choices)

 player = input("rock, paper, scissor?: ").lower()
 if player == computer:

        print("computer: ", computer)
        print("player: ", player)
        print("tie!")
 elif player == "rock":
      if computer == "paper":
          print("computer: ", computer)
          print("player: ", player)
          print("you lose!")
      if  computer == "scissor":
         print("computer: ", computer)
         print("player: ", player)
         print("you win!")
 elif player == "paper":
     if computer == "scissor":
         print("computer: ", computer)
         print("player: ", player)
         print("you lose!")
     if computer == "rock":
         print("computer: ", computer)
         print("player: ", player)
         print("you win!")
 elif player == "scissor":
     if computer == "rock":
         print("computer: ", computer)
         print("player: ", player)
         print("you lose!")
     if computer == "paper":
         print("computer: ", computer)
         print("player: ", player)
         print("you win!")
 else:
     print("false")
 play_again = input("play again (yes/no): ").lower()
 if play_again !=  "yes":
        break

print("Bye Coward!")