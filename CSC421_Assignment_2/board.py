class Board:
    """Summary
    
    Attributes:
        board (int): size of board
        ladders (dict): ladder list
        snakes (dict): snake list
    """
    def __init__(self):
        self.board = 0
        self.snakes = {}
        self.ladders = {}

    def getSnakes(self, id):
        return self.snakes[id]

    def getLadders(self, id):
        return self.ladders[id]

    def getSize(self):
        return self.board
