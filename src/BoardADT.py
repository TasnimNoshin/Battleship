#Tasnim Bari Noshin (400043624)
from PointADT import*

class BoardT:
    
    PointT = {"FREE", "SHIP", "MISS", "HIT"}
    traceShot = []
    shipList = [[],[],[],[],[]]
    shipSunk = 0
    switchTurn = True
    possible_ships = [2,3,3,4,5]
    
    def __init__(self):
        self.board= [["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"],
                    ["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"],
                    ["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"],
                    ["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"],
                    ["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"],
                    ["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"],
                    ["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"],
                    ["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"],
                    ["FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE","FREE"]]

    def placeShip(self,size,start,end):
        if(is_valid_ship(size,start,end,self.board) == 1):
                for i in range(0,end.ycrd()):
                    self.board[start.xcrd()][start.ycrd()+i] = "SHIP"
                    self.tempShip.append(pointT(start.xcrd(),start.ycrd()+i))
        else:
            for i in range(0,end.xcrd()):
                self.board[start.xcrd()+i][start.ycrd()] = "SHIP"
                self.tempShip.append(pointT(start.xcrd()+i,start.ycrd()))

    
    def shotTaken(self,move,opBoard):
        if(is_valid_move(move,self.board) and opBoard[move.xcrd()][move.ycrd()] == "SHIP"):
            opBoard[move.xcrd()][move.ycrd()] = "HIT"
            for ship in shipList:
                    del ship[move]
        else:
            opBoard[move.xcrd()][move.ycrd()] = "MISS"
        self.traceShot.append(move)
        self.switchTurn = not(self.switchTurn)
            
    
    
    def getTraceShot(self):
        return self.traceShot

    def getBoard(self):
        return self.board

    def addToShipList(self,ship):
        self.shipList.append(ship)

    def getShipList(self):
        return self.shipList

    def hasSunk(self,ship):
        if(ship in self.shipList and len(ship) == 0):
            self.shipSunk = self.shipSunk + 1

    def turn(self):
        return self.switchTurn

    def isLosing(self):
        try:
            if(self.shipSunk == Constants.SHIP_NUMBER):
                return True
        except:
            if(self.shipSunk > Constants.SHIP_NUMBER):
                print('This ship is invalid')

    def chances(self):
        return ((self.shipSunk/Constants.SHIP_NUMBER)*100)
            
            
def is_valid_ship(size,start,end,board):
        try:
            if(end.xcrd() == start.xcrd()):
                return 1
            else:
                return 2
        except:
            if(size not in self.possible_ships):
                print('This ship is invalid')
            if(end.ycrd() > Constants.MAX_BOARD_COLUMNS or start.ycrd() > Constants.MAX_BOARD_COLUMNS):
                print('point out of bound')
            if(end.xcrd() > Constants.MAX_BOARD_ROWS or start.xcrd() > Constants.MAX_BOARD_ROWS):
                print('point out of bound')
            if(end in self.shipList or start in self.shipList):
                print('This move is invalid')
        
            if(end.xcrd() != start.xcrd() or end.xcrd() != start.ycrd()):
                print('This ship is invalid')

def is_valid_move(move,board):
        try:
            return True
        except:
            if(move.ycrd() > Constants.MAX_BOARD_COLUMNS):
                print('point out of bound')
            if(move.xcrd() > Constants.MAX_BOARD_ROWS):
                print('point out of bound')
            if(move in self.board):
                print('This move is invalid')
