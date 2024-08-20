import random

def getcomputerchoice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def winner(userchoice, computerchoice):
    if userchoice == computerchoice:
        return 'tie'
    if (userchoice == 'rock' and computerchoice == 'scissors') or \
       (userchoice == 'scissors' and computerchoice == 'paper') or \
       (userchoice == 'paper' and computerchoice == 'rock'):
        return 'user'
    return 'computer'

def display(userchoice, computerchoice, result):
    print(f"\nYour choice: {userchoice}")
    print(f"Computer's choice: {computerchoice}")
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("Computer wins")

def main():
    userscore = 0
    computerscore = 0
    playagain = 'yes'

    while playagain.lower() == 'yes':
        userchoice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        if userchoice not in ['rock', 'paper', 'scissors']:
            print(" Please enter rock, paper, or scissors.")
            continue

        computerchoice = getcomputerchoice()
        result = winner(userchoice, computerchoice)
        display(userchoice, computerchoice, result)

        if result == 'user':
            userscore += 1
        elif result == 'computer':
            computerscore += 1

        print(f"\nScores: You - {userscore}, Computer - {computerscore}")
        playagain = input("Do you want to play again? (yes/no): ")

    

if __name__ == "__main__":
    main()

