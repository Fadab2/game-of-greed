from random import randint
#from game_logic import GameLogic.calculate_score

class Game:

    def default_roller():
        return (randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))
    

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
                roll = roller()
                roller_str = ''
                for num in roll:
                    roller_str += str(num) + " "
                print(f'Starting round {counter}')
                print(f'Rolling {6} dice...')

                print(f'*** {roller_str} ***')
                print("Enter dice to keep, or (q)uit:")
                choice = input("> ")
                if choice == "q":
                    print("Thanks for playing. You earned 0 points")
                    break
                



# if __name__ == "__main__":
#     rolls = [(4,),(4,), (5,),(2,), (3,),(1,)]  # 4 4 5 2 3 1
    

#     def mock_roller():
#         # return (4,3, 1, 1)
#         return rolls.pop(0) if rolls else Game.default_roller()
    
#     Game.play()
    