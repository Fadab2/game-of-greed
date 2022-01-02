
from random import choice
from game_logic import GameLogic
from banker import Banker


class Game:
    def __init__(self):
        self.banker = Banker()
        self.rounds = 0
        self.amount_of_dice = 6


    def default_roller(self):
        return GameLogic.roll_dice(self.amount_of_dice)

    def quiter(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")

    def decline(self):
        print("OK. Maybe another time")

    def play(self, roller=GameLogic.roll_dice):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        response = input('> ')

        if response == 'n' or response == 'no':
            print("OK. Maybe another time")
        elif response == 'y' or response == 'yes':
            self.play_game(roller)

    def play_game(self, roller):
        while True:
            self.rounds += 1

            print(f'Starting round {self.rounds}')
            print(f'Rolling {self.amount_of_dice} dice...')

            roll = roller(self.amount_of_dice) #check this out
            roller_str = ''
            for num in roll:
                roller_str += str(num) + " "
            print(f'*** {roller_str}***')

            print("Enter dice to keep, or (q)uit:")
            choice = input("> ")

            if choice == "q":
                self.quiter()
                break

            else:
                list_of_choices = tuple(map(int, list(choice)))
                self.amount_of_dice -= len(list_of_choices)
                score = GameLogic.calculate_score(list_of_choices)
                print(f'score: {score}')
                self.banker.shelf(score)
                print(f'You have {self.banker.shelved} unbanked points and {self.amount_of_dice} dice remaining')
                print(f'(r)oll again, (b)ank your points or (q)uit:')
                choice = input("> ")

                if choice == 'b' or choice == 'bank':
                    self.banker.bank()
                    self.amount_of_dice = 6
                    print(f'You banked {self.banker.shelved} points in round {self.rounds}')
                    print(f'Total score is {self.banker.balance} points')

                elif choice == 'r' or choice == 'roll':
                    pass

                elif choice == 'q' or choice == 'quit':
                    self.quiter()
                    break

                # 
                # print(f'list of respones: {list_of_respones}')
                # print(len(f'roll: {roll}'))
                # print(f'old amount of dice: {self.amount_of_dice}')
                # print(f'new amount of dice: {self.amount_of_dice}')

if __name__ == '__main__':
    run = Game()
    run.play()

