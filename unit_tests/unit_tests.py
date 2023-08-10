import numpy as np
import pandas as pd

import unittest
from montecarlo import Dice
from montecarlo import Game
from montecarlo import Analyzer

class TestDice(unittest.TestCase):
    '''
    This class provides a number of unit tests to ensure the functionality of the dice class
    '''
    
    def test_init(self):
        '''
        PURPOSE: ensure the Dice class is producing the dice object when initialized
        INPUT: none
        OUTPUT: a true assertion
        '''
        arr = np.array([1, 3, 5, 7, 9])
        dice1 = Dice(arr)
        
        self.assertTrue(isinstance(dice1, Dice))
    
    def test_change_weights(self):
        '''
        PURPOSE: ensure the change weights method of the Dice class works properly
        INPUT: none
        OUTPUT: an equal assertion
        '''
        arr = np.array([1, 3, 5, 7, 9])
        dice1 = Dice(arr)
        dice1.change_weights(1, 2)
        
        expected = 2.0
        actual = dice1.dice_df['weights'][0]
        self.assertEqual(expected, actual)
        
    def test_roll_dice(self):
        '''
        PURPOSE: ensure the roll dice method of the Dice class works properly
        INPUT: none
        OUTPUT: a true assertion
        '''
        arr = np.array([1, 3, 5, 7, 9])
        dice1 = Dice(arr)
        
        diceroll = dice1.roll_dice()
        result_type = list
        
        self.assertTrue(isinstance(diceroll, result_type))
        
    def test_print_dice(self):
        '''
        PURPOSE: ensure that the print dice method of the dice class works properly
        INPUT: none
        OUTPUT: a true assertion
        '''
        arr = np.array([1, 3, 5, 7, 9])
        dice1 = Dice(arr)
        
        diceroll = dice1.roll_dice(3)
        dice_results = dice1.print_dice()
        data_type = pd.core.frame.DataFrame
        
        self.assertTrue(isinstance(dice_results, data_type))
        
if __name__ == '__main__':
    unittest.main(verbosity = 3)
    
class TestGame(unittest.TestCase):
    '''
    This class is a series of unit tests to ensure the functionality of the Game class
    '''
    
    def test_init(self):
        '''
        PURPOSE: test the initialization of the game class
        INPUT: none
        OUTPUT: a true assertion
        '''
        dice1 = Dice(np.array([1, 3, 5, 7, 9]))
        dice2 = Dice(np.array([4, 1, 2, 7, 3]))
        dice3 = Dice(np.array([3, 5, 7, 2, 9]))
        dicelist = [dice1, dice2, dice3]
        game1 = Game(dicelist)
        
        self.assertTrue(isinstance(game1, Game))
    
    def test_play(self):
        '''
        PURPOSE: test the play method of the game class
        INPUT: none
        OUTPUT: equal assertion
        '''
        dice1 = Dice(np.array([1, 3, 5, 7, 9]))
        dice2 = Dice(np.array([4, 1, 2, 7, 3]))
        dice3 = Dice(np.array([3, 5, 7, 2, 9]))
        dicelist = [dice1, dice2, dice3]
        game1 = Game(dicelist)
        
        gameplay = game1.play(3)
        expected = 3
        self.assertEqual(len(gameplay), expected)
        
    def test_recent_play(self):
        '''
        PURPOSE: test the recent play method of the game class
        INPUT: none
        OUTPUT: two equal assertions
        '''
        dice1 = Dice(np.array([1, 3, 5, 7, 9]))
        dice2 = Dice(np.array([4, 1, 2, 7, 3]))
        dicelist = [dice1, dice2]
        game1 = Game(dicelist)
        gameplay = game1.play(3)
        game_recent1 = game1.recent_play(form = "wide")
        game_recent2 = game1.recent_play(form = "narrow")
        len1 = 3
        len2 = 6
        
        self.assertEqual(len(game_recent1), len1)
        self.assertEqual(len(game_recent2), len2)
        
if __name__ == '__main__':
    unittest.main(verbosity = 3)
    
    
class TestAnalyzer(unittest.TestCase):
    '''
    This class is a series of unit tests to ensure the functionality of the analyzer class
    '''
    
    def test_init(self):
        '''
        PURPOSE: test the initialization of the Analyzer class
        INPUT: none
        OUTPUT: a true assertion
        '''
        dice1 = Dice(np.array([1, 3, 5, 7, 9]))
        dice2 = Dice(np.array([4, 1, 2, 7, 3]))
        dice3 = Dice(np.array([3, 5, 7, 2, 9]))
        dicelist = [dice1, dice2, dice3]
        game1 = Game(dicelist)
        gameplay = game1.play(3)
        game_recent1 = game1.recent_play(form = "wide")
        ana1 = Analyzer(game1)
        
        self.assertTrue(isinstance(ana1, Analyzer))
    
    def test_jackpot(self):
        '''
        PURPOSE: test the jackpot method of the Analyzer class
        INPUT: none
        OUTPUT: a true assertion
        '''
        dice1 = Dice(np.array([1, 3, 5, 7, 9]))
        dice2 = Dice(np.array([4, 1, 2, 7, 3]))
        dice3 = Dice(np.array([3, 5, 7, 2, 9]))
        dicelist = [dice1, dice2, dice3]
        game1 = Game(dicelist)
        gameplay = game1.play(3)
        game_recent1 = game1.recent_play(form = "wide")
        ana1 = Analyzer(game1)
        test = ana1.jackpot()
        
        self.assertTrue(isinstance(test, int))
        
    def test_facecount(self):
        '''
        PURPOSE: test the face counting maethod of the Analyzer class
        INPUT: none
        OUTPUT: a true assertion
        '''
        dice1 = Dice(np.array([1, 3, 5, 7, 9]))
        dice2 = Dice(np.array([4, 1, 2, 7, 3]))
        dice3 = Dice(np.array([3, 5, 7, 2, 9]))
        dicelist = [dice1, dice2, dice3]
        game1 = Game(dicelist)
        gameplay = game1.play(3)
        game_recent1 = game1.recent_play(form = "wide")
        ana1 = Analyzer(game1)
        test = ana1.facecount()
        
        self.assertTrue(isinstance(test, pd.core.frame.DataFrame))
    
    def test_combos(self):
        '''
        PURPOSE: test the combination counting method of the Analyzer class
        INPUT: none
        OUTPUT: a true assertion
        '''
        dice1 = Dice(np.array([1, 3, 5, 7, 9]))
        dice2 = Dice(np.array([4, 1, 2, 7, 3]))
        dice3 = Dice(np.array([3, 5, 7, 2, 9]))
        dicelist = [dice1, dice2, dice3]
        game1 = Game(dicelist)
        gameplay = game1.play(3)
        game_recent1 = game1.recent_play(form = "wide")
        ana1 = Analyzer(game1)
        test = ana1.combos()
        
        self.assertTrue(isinstance(test, pd.core.frame.DataFrame))
    
    def test_perms(self):
        '''
        PURPOSE: test the permutation counting method of the analyzer class
        INPUT: none
        OUTPUT: a true assertion
        '''
        dice1 = Dice(np.array([1, 3, 5, 7, 9]))
        dice2 = Dice(np.array([4, 1, 2, 7, 3]))
        dice3 = Dice(np.array([3, 5, 7, 2, 9]))
        dicelist = [dice1, dice2, dice3]
        game1 = Game(dicelist)
        gameplay = game1.play(3)
        game_recent1 = game1.recent_play(form = "wide")
        ana1 = Analyzer(game1)
        test = ana1.perms()
        
        self.assertTrue(isinstance(test, pd.core.frame.DataFrame))
        

if __name__ == '__main__':
    unittest.main(verbosity = 3)
        
        