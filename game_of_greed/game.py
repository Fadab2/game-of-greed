from random import randint
from game_of_greed.game_logic import GameLogic

class Game:

    def default_roller(dice=6):
        return GameLogic.roll_dice(dice)
    
    def play(self, roller=default_roller):
        print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        counter = 0
        while True:
            response = input("> ")
            if response == "n" or response == "no":
                print("OK. Maybe another time")
                break
            elif response == "y" or response == "yes":
                counter += 1
                # print(f'roller: {roller}')
                roll = roller(self) #check this out
                # print(f'roll: {roll}')
                roller_str = ''
                for num in roll:
                    roller_str += str(num) + " "
                print(f'Starting round {counter}')
                print(f'Rolling {6} dice...')

                print(f'*** {roller_str}***')
                print("Enter dice to keep, or (q)uit:")
                choice = input("> ")
                if choice == "q":
                    print("Thanks for playing. You earned 0 points")
                    break


if __name__ == "__main__":
    rolls = [(4,4,5,2,3,1)]  # 4 4 5 2 3 1
    

    def mock_roller():
        return (4,3, 1, 1)
        # return rolls.pop(0) if rolls else Game.default_roller()
    
    Game.play(mock_roller)
    