import random
import math
import numpy
from board import Board


def diceRoll(sides):
    """Summary
    
    Args:
        sides (TYPE): The number of sides a dice
    
    Returns:
        TYPE: One of the number of sides of the based on a uniform distribution between 0 and 1
    """
    distribution = random.random()
    total = 0
    dice_result = 1
    for i in range(sides):
        total = total + 1 / float(sides)
        if distribution < total:
            return dice_result
        dice_result = dice_result + 1


def playGame(board, dice_sides):
    """Summary
    
    Args:
        board (TYPE): Board Object
        dice_sides (TYPE): Number of sides on the dice
    
    Returns:
        TYPE: Runs the snake and ladder game and returns the number of dice rolls
        it took to finish the game
    """
    start = 0
    num_rolls = 0
    while start < board.getSize():
        start = start + diceRoll(dice_sides)
        if start in board.snakes.keys():
            start = board.getSnakes(start)
        elif start in board.ladders.keys():
            start = board.getLadders(start)
        num_rolls = num_rolls + 1
    return num_rolls


def setOfGames(board, num_of_games, dice_sides):
    """Summary
    
    Args:
        board (TYPE): Board Object
        num_of_games (TYPE): Number of game simulations to run
        dice_sides (TYPE): The number of sides the dice has
    
    Returns:
        TYPE: A list of game simulation outcomes with the number of dice rolls it took
        to complete the game
    """
    l = []
    for i in range(num_of_games):
        l.append(playGame(board, dice_sides))
    return l


def getAverage(list_of_games):
    """Summary
    
    Args:
        list_of_games (TYPE): A list with the number of dice rolls it took to 
        complete the game
    
    Returns:
        TYPE: The average number of dice rolls to complete the game
    """
    return sum(list_of_games) / float(len(list_of_games))


def getAverageStd(list_of_games, average):
    """Summary
    
    Args:
        list_of_games (TYPE): A list with the number of dice rolls it took to 
        complete the game
        average (TYPE): The average number of dice rolls to complete the game
    
    Returns:
        TYPE: The average standard deviation of the number of dice rolls to complete
        the game
    """
    variance = map(lambda x: (x - average)**2, list_of_games)
    avg_std = getAverage(variance)
    return math.sqrt(avg_std)


def main():
	# values of the snakes and ladders
    snakes = [(16, 6), (48, 26), (49, 11), (56, 53), (62, 10),
              (64, 60), (87, 24), (93, 73), (95, 75), (98, 78)]
    ladders = [(1, 38), (4, 14), (9, 31), (21, 42), (28, 84),
               (36, 44), (51, 67), (71, 91), (80, 100)]
    board = Board()
    board.board = 100
    board.snakes = dict(snakes)
    board.ladders = dict(ladders)
    l = setOfGames(board, 1000, 6)
    l_dictionary = {}
    for i in l:
    	l_dictionary[i] = l_dictionary.get(i, 0) + 1
    print l
    average = getAverage(l)
    print "Average: " + str(average)
    print "Standard Deviation: " + str(getAverageStd(l, average))


if __name__ == "__main__":
    main()
