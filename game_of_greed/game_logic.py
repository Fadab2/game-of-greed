import collections
import sys
from math import pi
import random
from collections import Counter

from attr import s

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
    count_dices = 0
    @staticmethod # staticmethod doesn't belong to a single instance
    def roll_dice(rolled_dice=None):
        dice_list = []
        for _ in range(rolled_dice):
            dice_list.append(random.randint(1,6))
            # print(dice_list)
        return tuple(dice_list)
    

    '''
    This Method will Calculate the score using the roll_dice method above to get each die value then it will check against the dictionary values to get that new score of the rolled dice
    it has two if statements that will handle pairs and a straight
    '''
    @staticmethod
    def calculate_score(roll_dice):
        score_values = game_logic_dict
        score = 0
        pairs = 0
        counts = collections.Counter(roll_dice) # {1:2, 3:2, 6:1, 5:1}, 
        '''This first if statement will handle if we get a straight for the dice'''
        if len(counts) == 6:
            score += 1500
            return score
        '''This next if statment will handle any pairs to get the right score'''
        for i in counts:
            if counts[i] == 2:
                pairs += 1
                if pairs == 3:
                    score += 1500
                    return score
        '''this for loop will check against the dictionary for any values that are not a straight or pairs'''
        for die, count in counts.items():
            score += score_values[die][count]
            #print(score)

        return score
    
    @staticmethod
    def validate_keepers(roll, keepers):
        keeper_counter = Counter(keepers)
        roll_counter = Counter(roll)
        results = keeper_counter - roll_counter # 1:3,2:1,4:1,5:1 # 1:3 = 2 4 5 not result 
        return not results
    
    @staticmethod
    def get_scorers(dice):
        total_score = GameLogic.calculate_score(dice)
        if total_score == 0:
            return tuple()
        list_of_scores = []
        for number in range(len(dice)):
            rolls = dice[:number] + dice[number + 1:]
            score = GameLogic.calculate_score(rolls)
            if score != total_score:
                list_of_scores.append(dice[number])
        return tuple(list_of_scores)



if __name__ == "__main__":
    GameLogic.choose_dice((2,1,4,5,6,5))
