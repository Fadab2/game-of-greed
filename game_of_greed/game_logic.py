import collections
import random
from collections import Counter

game_logic_dict = {
    1: {
        1:100, 
        2:200, 
        3:1000,
        4:2000, 
        5:3000, 
        6:4000
    }, 
    2: {
        1:0,
        2:0,
        3:200, 
        4:400, 
        5:600,
        6:800
    }, 
    3: {
        1:0,
        2:0,
        3:300,
        4:600, 
        5:900,
        6:1200
    }, 
    4: {
        1:0,
        2:0,
        3:400, 
        4:800,
        5:1200, 
        6:1600,
    }, 
     5: {
        1:50, 
        2:100, 
        3:500, 
        4:1000,
        5:1500,
        6:2000
    }, 
    6: {
        1:0,
        2:0,
        3:600, 
        4:1200, 
        5:1800,
        6:2400
    }
}


class GameLogic:

    @staticmethod
    def roll_dice(rolled_dice):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
            # print(dice_list)
        return tuple(dice_list)
    


    @staticmethod
    def calculate_score(roll_dice):
        score_values = game_logic_dict
        score = 0
        counts = collections.Counter(roll_dice)
        if len(counts) == 6:
            score += 1500
            return score
        for die, count in counts.items():
            score += score_values[die][count]
            #print(score)

        return score
       


    # we make a dict 1:!!, 2:!! -> 6
    # If a player rolls all 6 of the same dice in 1 roll the game is automatically over no player gets a last roll
    # Double Trips when 2 sets of 3 of a kind are hit. Scores are added together and doubled.
    # A straight from 1 to 6 is worth 1500 points
    # Three pairs are worth 1000 points
    # dice from later rolls do not "stack" for the higher score. (each roll is independent)

    # one_and_five = {
    #     1:100, 5:50
    # }
    # three_of_same = {
    #     1:1000,
    #     2:200,
    #     3:300,
    #     5:500,
    #     4:400,
    #     6:600
    # }
    # four_of_same = {
    #     1:three_of_same[1] * 2,
    #     2:three_of_same[2] * 2,
    #     3:three_of_same[3] * 2,
    #     4:three_of_same[4] * 2,
    #     5:three_of_same[5] * 2,
    #     6:three_of_same[6] * 2
    # }

    # five_of_same = {
    #     1:four_of_same[1] * 2,
    #     2:four_of_same[2] * 2,
    #     3:four_of_same[3] * 2,
    #     4:four_of_same[4] * 2,
    #     5:four_of_same[5] * 2,
    #     6:four_of_same[6] * 2
    # }
    # six_of_same = {
    #     1:five_of_same[1] * 2,
    #     2:five_of_same[2] * 2,
    #     3:five_of_same[3] * 2,
    #     4:five_of_same[4] * 2,
    #     5:five_of_same[5] * 2,
    #     6:five_of_same[6] * 2
    # }


if __name__ == "__main__":

    print(GameLogic.calculate_score((1,1,1,2, 3, 4)))

    # print(GameLogic.roll_dice(4))

    # keys = (Counter(GameLogic.roll_dice(6)))
    
    # for key in keys:
        
    #   print(keys[key] * 100)

    # for item , value in GameLogic.four_of_same.items():
    #     print("four of " ,item, "=", value)
    # print("******************")
    # for item , value in GameLogic.five_of_same.items():
    #     print("five of " ,item, "=", value)
        
    # print("******************")
    # for item , value in GameLogic.six_of_same.items():
    #     print("six of " ,item, "=", value)
        
    #     print((Counter(GameLogic.roll_dice(6))))
    
    #     print(len((Counter(GameLogic.roll_dice(6)))))
        