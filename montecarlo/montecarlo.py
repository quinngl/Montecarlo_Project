import numpy as np
import pandas as pd
class Dice():
    '''
    This class creates a dice object with an editable number of faces. Methods include the ability to change the weight of a face, rolling the dice, and returning a dataframe with the faces and weights of the dice.
    '''
    
    
    def __init__(self, faces):
        '''
        PURPOSE: Initialize the object of the dice class
        INPUT: numpy array of unique objects of the same data type which will represent the dice
        '''
        self.faces = faces
        self.weights = np.ones(len(self.faces))
        data_type = type(faces[0])
        if not isinstance(faces, np.ndarray):
            raise TypeError("Input must be a numpy array")
        if not all(isinstance(item, data_type) for item in faces):
            raise ValueError("All items in the array must have the same data type.")
        if len(faces) != len(set(faces)):
            raise ValueError("All items in the array must be unique.")
        else:
            self.dice_df = pd.DataFrame({'faces': self.faces, 'weights':self.weights})
    
    def change_weights(self, n, w):
        '''
        PURPOSE: change the weight of a single face of the die.
        INPUT: n- the face to be changed in the method; w- the new weight of the face
        OUTPUT: a data frame displaying all the weights and faces of the dice
        '''
        typen = type(n)
        if n not in self.faces:
            raise IndexError("The given value is not a face on the die.")
        if not isinstance(n, int) | isinstance(n, float) | isinstance(n, str):
            raise TypeError("The data type of the given value does not match the data type of the die.")
        else:
            mask = self.dice_df['faces'] == n
            self.dice_df.loc[mask, 'weights'] = w
            return self.dice_df
        
    def roll_dice(self, rolls = 1):
        '''
        PURPOSE: "roll" the dice object
        INPUT: the number of rolls to be operated in the method; default = 1
        OUTPUT: a list of faces returned by the rolling operation
        '''
        results = []
        for i in range(rolls):
            result = self.dice_df.faces.sample(weights=self.dice_df.weights).values[0]
            results.append(result)
        return results
    
    def print_dice(self):
        '''
        PURPOSE: display the dataframe of the dice faces and weights
        INPUT: none
        OUTPUT: the dice dataframe
        '''
        return self.dice_df

class Game():
    '''
    This class takes a list of dice objects and returns the outputs of multiple rolled dice in different formats
    '''
    
    def __init__(self, dicelist):
        '''
        PURPOSE: to initialize the game class
        INPUT: a list of dice objects
        OUTPUT: a game object
        '''
        self.dicelist = dicelist
        if not isinstance(dicelist, list):
            raise TypeError("input must be a list")
        else:
            pass
    
    def play(self, r):
        '''
        PURPOSE: roll all the dice in the game and return a dataframe of the responses
        INPUT: the number of rolls
        OUTPUT: a dataframe with the roll outputs for each dice
        '''
        outcomes = []
        for i in self.dicelist:
            outcome = i.roll_dice(rolls = r)
            outcomes.append(outcome)
            self.plays = pd.DataFrame({f'Dice {i}': sublist for i, sublist in enumerate(outcomes)})
            self.plays.index.name = "Roll"
        return self.plays
    
    def recent_play(self, form = "wide"):
        '''
        PURPOSE: create a data frame of all the recent plays of the play method
        INPUT: the table format of the data frame; default = wide
        OUTPUT: a dataframe of recent plays
        '''
        if form == "narrow":
            self.indexed = self.plays.reset_index()
            self.narrow_df = pd.melt(self.indexed, id_vars = ['Roll'], var_name = 'Dice', value_name='Play_Result').reset_index()
            self.narrow_df = self.narrow_df.pivot_table(index = ['Roll', 'Dice'],
                                                          values = 'Play_Result')
            return self.narrow_df
        if form == "wide":
            return self.plays
        else:
            raise ValueError('Form must be either narrow or wide')

class Analyzer():
    '''
    A class that calculates various statistical values from the output of the game class
    '''
    
    def __init__(self, game):
        '''
        PURPOSE: Initialize the analyzer class
        INPUT: a game object
        OUTPUT: an analyzer class instance
        '''
        self.game = game
        data_type = Game
        if not isinstance(self.game, data_type):
            raise ValueError("Attribute must be an object instance from the Game class")
        else:
            pass
        
    def jackpot(self):
        '''
        PURPOSE: identify rolls where all the dice returned the same face (a jackpot)
        INPUT: none
        OUTPUT: a value count of all rolls that have the same number (a jackpot count)
        '''
        count = 0
        for index, row in self.game.plays.iterrows():
            if all(value == row.iloc[0] for value in row):
                count += 1
        return count
    
    def face_count(self):
        '''
        PURPOSE: Count the number of times a face value appeared for each roll
        INPUT: none
        OUTPUT: a dataframe displaying the counts for each time a face appeared in the rolls
        '''
        mygame = self.game.recent_play(form = "narrow").groupby('Roll').value_counts().reset_index().rename({0:'Count'}, axis = 1)
        mygame = mygame.pivot_table(index = 'Roll',
                                   columns = 'Play_Result',
                                   values = 'Count')
        mygame = mygame.fillna(0)
        return mygame
    
    def combos(self):
        '''
        PURPOSE: identify the combinations of different faces within a game
        INPUT: none
        OUTPUT: a multi-index dataframe
        '''
        cdict = {}
        for _,roll in self.game.plays.iterrows():
            c = tuple(sorted(roll.tolist()))
            if c in cdict:
                cdict[c] += 1
            else:
                cdict[c] = 1
        mycombos = pd.DataFrame(cdict.values(),
                                index = pd.MultiIndex.from_tuples(cdict.keys()),
                                columns = ["Count"])
        return mycombos
    
    def perms(self):
        '''
        PURPOSE: identify the permutations of different faces within the game
        INPUT: none
        OUTPUT: a multi-index dataframe
        '''
        myplays = self.game.recent_play(form = "wide")
        myperms = myplays.groupby(myplays.columns.tolist()).value_counts()
        myperms = pd.DataFrame(myperms)
        return myperms