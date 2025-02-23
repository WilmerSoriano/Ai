import os
import sys

#3.0 List of available Algorithms
def BFS(Start, Goal, flag):
   visited = list()
   queue = [Start]

   while queue:

      checkSet = queue.pop(0)
      print(checkSet, end= " ")

      if checkSet == Goal:
         print("Complete:" + str(checkSet))
         return 1
      else:
         visited.append(checkSet)
      
      #Generate all possible successors and play the game
      for move in ["up", "down", "left", "right"]:
         newGame = puzzleGame(checkSet)

         #if False, the move was invalid
         if newGame.moves(move):
            newSet = list(newGame.set)
            if newSet not in visited:
               queue.append(newSet)

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

   def moves(self, direction):
      CurrentIndex = self.ZeroLocation()
      newSet = list(self.set)
      """
      index at 0 = [1,1]
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

      #
      posZero_x, posZero_y = divmod(CurrentIndex,3)
      move = moves.get(direction)

      if move:
         newPos_x = posZero_x + move[0]
         newPos_y = posZero_y + move[1]

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
            numbers.append(int(num)) # Changed to int to find Zero
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