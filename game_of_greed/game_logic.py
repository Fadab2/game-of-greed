import collections
from math import pi
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
        counts = collections.Counter(roll_dice)
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
    def choose_dice(rolled_dice):
        store_dice = []
        picked_value = input("Enter dice to keep, or (q)uit:")
    
       
        for char in picked_value:
            store_dice.append(char)
            
        d = Counter(rolled_dice)
        for dice in d.elements():
            if dice in store_dice:
               print(dice)
               
            # if len(d):
            #    
            #     if picked_value == 'q':
            #         print("Thanks for playing. You earned 0 points")
            #     # 4 2 6 4 5 5
            #     get_to_keep = GameLogic.calculate_score(picked_value)
            #     print("get to keep", get_to_keep)
            #     # we need to subtract the picked up dices from the length (roll the remaining dices)
            #     dices_on_hand = len(store_dice) - len(get_to_keep)
            #     print(f'You have {get_to_keep} unbanked points and {dices_on_hand} dice remaining')
            #     print("(r)oll again, (b)ank your points or (q)uit:")

    

if __name__ == "__main__":

    print(GameLogic.calculate_score((2,1,4,3,6,5)))
    GameLogic.choose_dice((2,1,4,5,6,5))