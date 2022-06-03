import random


def start():
    while True:
        user_input = input("Enter A choice (R,P,S)")
        possible_choice = ["R", "P", "S"]
        computer_choice = random.choice(possible_choice)
        #print(f"\nYou chose {user_input}. Computer chose {computer_choice}")

        # Conditions for wining the game
        if user_input == computer_choice:
            print(
                f" You selected {user_input}: CPU seleceted {computer_choice}. Its a Tie")
            start()
        elif user_input == "R":
            if computer_choice == "S":
                print(
                    f" You selected {user_input}: CPU seleceted {computer_choice}")
                print("Rock Smashes scissors ! You win!!! ")

            else:
                print(
                    f" You selected {user_input}: CPU seleceted {computer_choice}")
                print("paper Covers rock!! You lose!!!")
        elif user_input == "P":
            if computer_choice == "R":
                print(
                    f" You selected {user_input}: CPU seleceted {computer_choice}")
                print("Paper covers Rock!!! You win")
            else:
                print(
                    f" You selected {user_input}: CPU seleceted {computer_choice}")
                print("scissors cuts Paper!! You lose!!!")
        elif user_input == "S":
            if computer_choice == "P":
                print(
                    f" You selected {user_input}: CPU seleceted {computer_choice}")
                print("Scissors cuts paper! You win")
            else:
                print(
                    f" You selected {user_input}: CPU seleceted {computer_choice}")
                print("Rock smashes Scissors!! You Lose!!. ")
        else:
            print("Invalid Response Please Enter a valid Choice")
            user_input = input("Enter A choice (R,P,S)")

        play_again = input("Do You want to play again? (y/n):")
        if play_again.lower() != "y":
            break


start()
