import os
import sys

#3.0 List of available Algorithms
def BFS(Start, Goal, flag):
   print(Start[4])
   newGame = puzzleGame(Start)
   newGame.moves("up")

def UCS(Start, Goal, flag):
   print("Hello UCS")

def Greedy(Start, Goal, flag):
   print("Hello greedy")

def A_Star(Start, Goal, flag):
   print("Hello A*")

#3.1 Create the game/rule of the game in OOP style
""" 
   NOTE:
   Recommed playing 8-puzzle game to
   understand rules and mechanics.

   Zero would be our perspective 

"""
class puzzleGame:
   # Constructor to initialize values
   def __init__(self, Sets):
      self.set = Sets

   # Look for 0 within array, 0 will be our mover
   def ZeroLocation(self):
      return self.set.index(0)
   
   # Creating the 8 puzzle board game in 2D array
   def constructBoard(self):
      doubleArry = [[0 for i in range(3)] for j in range(3)]
      for x in range(3):
         for y in range(3):
            doubleArry[x][y] = self.set[x*3+y]
            
      return doubleArry

   def moves(self, direction):
      CurrentIndex = self.ZeroLocation()
      print(CurrentIndex)
      newSet = list(self.set)
      print(newSet)

      """
      index at 0 = [1][1]
      2 3 6
      1 0 7
      4 8 5
      """
      moves = {
         'up':[-1, 0], 
         'down':[1, 0],
         'left':[0, -1],
         'right':[0, 1]
      }

      # Check cu
      posZero_x, posZero_y = divmod(CurrentIndex,3)

      move = moves.get(direction)
      if move:
         newPos_x = posZero_x + move[1]
         newPos_y = posZero_y + move[0]

         # Check if move is within bound of game, CUDA method for 1D
         if 0 <= newPos_x < 3 and 0 <= newPos_y < 3:
            # Calculate the offset of new index
            newIndex = newPos_y*3 + newPos_x;
            
            # Swap Zero with the moving position and update the Set with new position
            newSet[CurrentIndex], newSet[newIndex] = newSet[newIndex], newSet[CurrentIndex]
            self.set = tuple(newSet)
            return True
      return False

# 2.0 Identify Algorithm
def Algorithms(argv, flag):
   Start = extractNum(argv[1])
   Goal = extractNum(argv[2])

   # If no algorithm inputed, default to A*
   if len(argv) < 4:
      A_Star(Start, Goal, flag)
   else:
      match argv[3]:
         case "bfs":
            BFS(Start, Goal, flag)
         case "ucs":
            UCS(Start, Goal, flag)
         case "greedy":
            Greedy(Start, Goal, flag)
         case "a*":
            A_Star(Start, Goal, flag)

#2.1 Extract the numbers from the file
def extractNum(file):
   numbers = []
   f = open(file, "r")
   for line in f:
      if line != "END OF FILE":
         for num in line.split():
            numbers.append(int(num))
   f.close()
   return numbers

# 1. Check all user arguments 
if __name__ == "__main__":
   
   # Catch exception:
   argv = sys.argv
   if  argv[1] != "start.txt":
      print("Error: Start file missing")
      exit -1
   elif  argv[2] != "goal.txt":
      print("Error: Goal file mssing")
      exit -1
   
   # Check if dump-flag was set
   flag = 0
   if len(argv) == 5:
      flag = argv[4]
   
   Algorithms(argv, flag)