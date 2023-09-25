player1 = input("Player 1 Name: ")
player2 = input("Player 2 Name: ")
p1Score = 0
p2Score = 0

while True:
    print(player1, "score:", p1Score)
    print(player2, "score:", p2Score)
    from getpass import getpass as input
    player1Turn = input("> ").lower()
    player2Turn = input("> ").lower()
    if player1Turn == "rock" or player1Turn == "r":
        if player2Turn == "rock" or player2Turn == "r":
            print("You both chose ROCK! Try again")
            continue
        if player2Turn == "paper" or player2Turn == "p":
            print(player1, "chose ROCK.", player2, "chose PAPER. 1 point to",
                  player2)
            p2Score += 1
            continue
        elif player2Turn == "scisssors" or player2Turn == "s":
            print(player1, "chose ROCK.", player2,
                  "chose SCISSORS. 1 point to", player1)
            p1Score += 1
            continue
    elif player1Turn == "paper" or player1Turn == "p":
        if player2Turn == "rock" or player2Turn == "r":
            print(player1, "chose PAPER.", player2, "chose ROCK. 1 point to",
                  player1)
            p1Score += 1
            continue
        elif player2Turn == "paper" or player2Turn == "p":
            print("You both chose PAPER! Try again")
            continue
        elif player2Turn == "scissors" or player2Turn == "s":
            print(player1, "chose PAPER.", player2,
                  "chose SCISSORS. 1 point to", player2)
            p2Score += 1
            continue
    elif player1Turn == "scissors" or player1Turn == "s":
        if player2Turn == "rock" or player2Turn == "r":
            print(player1, "chose SCISSORS.", player2,
                  "chose ROCK. 1 point to", player2)
            p2Score += 1
            continue
        elif player2Turn == "paper" or player2Turn == "p":
            print(player1, "chose SCISSORS.", player2,
                  "chose PAPER. 1 point to", player1)
            p1Score += 1
            continue
        elif player2Turn == "scissors" or player2Turn == "s":
            print("You both chose SCISSORS! Try again")
    else:
        print("\033[32m ERROR: Invalid input, try again \033[37m")
        continue
