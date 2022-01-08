import sys
import collections
from typing import Counter
from random import choice
from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    def __init__(self):
        self.banker = Banker()
        self.rounds = 1
        self.amount_of_dice = 6

    def default_roller(self):
        return GameLogic.roll_dice(self.amount_of_dice)

    def quiter(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")

    def decline(self):
        print("OK. Maybe another time")

    def zilch(self):
       print("****************************************")
       print("**        Zilch!!! Round over         **")
       print("****************************************")
        

    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n" or response == "no":
            print("OK. Maybe another time")
        elif response == "y" or response == "yes":
            self.play_game(roller)

    def play_game(self, roller):
        print(f"Starting round {self.rounds}")
        while True:
            
            print(f"Rolling {self.amount_of_dice} dice...")

            roll = roller(self.amount_of_dice)  # check this out
            # get the count of each number in the current roll
            roll_counts = collections.Counter(roll)
            # print(roll_counts)
            roller_str = ""
            for num in roll:
                roller_str += str(num) + " "
            print(f"*** {roller_str}***")
            # total current roll score
            roll_score = GameLogic.calculate_score(roll)
            if roll_score == 0:
                self.banker.clear_shelf()
                Game.zilch(roller)

            if roll_score > 0:
                print("Enter dice to keep, or (q)uit:")
                choice = input("> ")

            if choice == "q":
                self.quiter()
                sys.exit(0)

            else:
                roll_counter = Counter(roll)
                count_choices = Counter(choice)
                # if not GameLogic.validate_input_dice(roll_counter, count_choices):
                #      print("Cheater!!! Or possibly made a typo...")

                #list_of_choices = tuple(map(int, list(choice)))
                if choice.isnumeric():
                    list_to_tuple = tuple([int(num) for num in choice])
               
                

                # print(count_choices)
                self.amount_of_dice -= len(choice)
                to_keep_score = GameLogic.calculate_score(list_to_tuple)
                self.banker.shelf(to_keep_score)
             
               

                # calculate to dices to keep score
                print(
                    f"You have {self.banker.shelved} unbanked points and {self.amount_of_dice} dice remaining"
                )
                print(f"(r)oll again, (b)ank your points or (q)uit:")
                choice = input("> ")

                if choice == "b" or choice == "bank":
                    # increment round and reset dices when user banks points.
                   
                    print(
                        f"You banked {self.banker.shelved} points in round {self.rounds}"
                    )
                    self.banker.bank()
                    self.rounds += 1
                    self.amount_of_dice = 6
                    print(f"Total score is {self.banker.balance} points")
                    print(f"Starting round {self.rounds}")
                elif choice == "r" or choice == "roll":
                    if self.amount_of_dice == 0:
                        self.amount_of_dice = 6
                    # if len(roll) == 0:
                    #     print("No dice remaing. Staring over")
                    #     self.amount_of_dice == 6
                    continue

                elif choice == "q" or choice == "quit":
                    self.quiter()
                    break

                # These were the print statements we used along the way to ge the code working again
                # print(f'list of respones: {list_of_respones}')
                # print(len(f'roll: {roll}'))
                # print(f'old amount of dice: {self.amount_of_dice}')
                # print(f'new amount of dice: {self.amount_of_dice}')
                # print(f'score: {score}')


if __name__ == "__main__":
    run = Game()
    run.play()
