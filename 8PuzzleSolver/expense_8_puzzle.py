import os
import sys
from datetime import datetime

Flag = 0
FileName = None

# === If flag was set true, print to file ====
def WriteToFile(info):
   global FileName

   if FileName is None:
      date = datetime.now()
      FileStr = date.strftime("trace-%m-%d-%Y-%I-%M_%p")
      FileName = f"{FileStr}.txt"
   
   with open(FileName, "a") as file:
      file.write(info)

def FormatQueue(checkSet, Action, expNode, genNode, N, parent):
   return f"< state = {checkSet}, action = Moved {Action} g(n) = {expNode}, d = {genNode}, f(n) = {N}, Parent = Pointer to {parent} >:\n"

#3.0 List of available Algorithms
def BFS(Start, Goal):
   visited = set()
   checkMove = ""
   info = ""
   popNode = 0
   expNode = 0
   genNode = 0
   cost = 0
   queue = [(Start, "Start", 0, 0, 0, None)]

   while queue:
      currentSet = queue.pop(0)
      checkSet, m, c, depth, f, parent = currentSet

      if Flag == 1:
         info += "Generating successors to " 
         info += FormatQueue(checkSet, checkMove, cost, depth, 0, parent)
         info += "\t\tFringe:[\n"

         #Clean up the string, to make progress faster
         if expNode % 1000 == 0:
            WriteToFile(info)
            print(popNode)
            info = ""

      if checkSet == Goal:
         solutionPath = []
         while currentSet is not None:
            solutionPath.append(currentSet)
            currentSet = currentSet[5]
         solutionPath.reverse()
         depSolution = len(solutionPath)

         print("Goal has been found " + str(checkSet))
         print("Node Popped:", popNode)
         print("Node Expanded:", expNode)
         print("Node Generated:", genNode)
         print("Max Fringe Size:", str(len(queue)))
         print(f"Solution Found at depth {depSolution} with cost of {cost}.")
         print("Steps:")
         for showMove in solutionPath:
            print(showMove[1])

         if Flag == 1:
            info += f"Goal Found: {checkSet}\n"
            WriteToFile(info)
         return 1
      
      visited.add(tuple(checkSet))
      popNode += 1
      succGen = 0

      #Generate all possible successors and play the game
      for move in ["up", "down", "left", "right"]:
         #if False, the move was invalid
         newGame = puzzleGame(checkSet)
         checkMove = newGame.moves(move)

         if checkMove:
            newSet = list(newGame.set)
            succGen += 1
            expNode += 1
            newDep = depth + 1
            if tuple(newSet) not in visited:
               genNode += 1
               queue.append((newSet, checkMove,  cost, newDep, 0, currentSet))
               chold, dhold = checkMove
               cost += chold

      if Flag == 1:
         info += "\t\t]\n"
         info += f"\t\t{succGen} successors generated\n"
         info += f"\t\tClosed: {list(visited)}\n\n"
         info += f"\t\tFringe:[\n"
         for state in queue:
            info += "\t\t\t"
            info += FormatQueue(state[0], state[1], state[2], state[3], state[4], state[5])
         info += f"\t\t]\n"

def UCS(Start, Goal):
   info = "SHOULD WORK"
   WriteToFile(info)

def Greedy(Start, Goal):
   print("Hello greedy")

def A_Star(Start, Goal):
   print("Hello A*")

#3.1 Create the game/rule of the game in OOP style
""" 
   NOTE:
   Self reminder, Zero would be our perspective/controller 
   although the other values are being moved.
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

            moved = newSet[CurrentIndex]
            return (moved, direction)
         
      return False

# 2.0 Identify Algorithm
def Algorithms(argv):
   Start = extractNum(argv[1])
   Goal = extractNum(argv[2])

   # If no algorithm inputed, default to A*
   if len(argv) < 4:
      A_Star(Start, Goal)
   else:
      match argv[3]:
         case "bfs":
            BFS(Start, Goal)
         case "ucs":
            UCS(Start, Goal)
         case "greedy":
            Greedy(Start, Goal)
         case "a*":
            A_Star(Start, Goal)

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
   if len(argv) == 5:
      Flag = int(argv[4])
      if Flag == 1:
         info = ""
         info += f"\nCommand-Line Arguments : [{argv[1]}, {argv[2]}, {argv[3]}, {argv[4]}]\n"
         info += f"Method Selected: { argv[3] }\n"
         info += f"Running { argv[3] }\n"
         WriteToFile(info)

   Algorithms(argv)