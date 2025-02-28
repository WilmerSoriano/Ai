import sys
import heapq
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

def Formatchild(succGen, visited, queue):
   info = ""
   info += f"\t\t{succGen} successors generated\n"
   info += f"\t\tClosed: {list(visited)}\n"
   info += f"\t\tFringe:[\n"
   for state in queue:
      info += "\t\t\t"
      info += FormatQueue(state[0], state[1], state[2], state[3], state[4], state[5])
   info += f"\t\t]\n"
   return info

def FormatResult(currentSet, checkSet, popNode, expNode, genNode, queue):
   #queue.append((newSet, checkMove,  chold, newDep, 0, currentSet)) REFRENCE
   info = ""
   solutionPath = []
   cost = 0

   while currentSet is not None:
      solutionPath.append(currentSet)
      currentSet = currentSet[5]
      
   solutionPath.reverse()
   depSolution = len(solutionPath)

   for MoveCost in solutionPath:
      cost += MoveCost[2]

   if Flag == 1:
      info += f"Goal has been found {checkSet}\n"
      info += f"Node Popped:{popNode}\n"
      info += f"Node Expanded:{expNode}\n"
      info += f"Node Generated:{genNode}\n"
      info += f"Max Fringe Size: {str(len(queue))}\n"
      info += f"Solution Found at depth {depSolution-1} with cost of {cost}.\n"
      info += "Steps:"
   print("Goal has been found " + str(checkSet))
   print("Node Popped:", popNode)
   print("Node Expanded:", expNode)
   print("Node Generated:", genNode)
   print("Max Fringe Size:", str(len(queue)))
   print(f"Solution Found at depth {depSolution-1} with cost of {cost}.") 
   print("Steps: ")

   for showMove in solutionPath:
      print("Move", showMove[1])
      if Flag == 1:
         info += f"Move {showMove[1]}\n"

   if Flag == 1:
      WriteToFile(info)

#3.0 List of available Algorithms
def BFS(Start, Goal):
   queue = [(Start, "Start", 0, 0, 0, None)]
   visited = set()
   info = ""
   popNode = 0
   expNode = 0
   genNode = 0

   while queue:
      popNode += 1
      currentSet = queue.pop(0)
      checkSet, checkMove, cost, depth, f, parent = currentSet

      if Flag == 1:
         info += "Generating successors to " 
         info += FormatQueue(checkSet, checkMove, cost, depth, 0, parent)

         # Clean up the info-string-type, to make progress faster
         if expNode % 500 == 0:
            WriteToFile(info)
            info = ""
   
      if checkSet == Goal:
         FormatResult(currentSet, checkSet, popNode, expNode, genNode, queue)
         return 1

      succGen = 0
      # Generate all possible successors and play the game
      for move in ["up", "down", "left", "right"]:
         newGame = puzzleGame(checkSet)
         checkMove = newGame.moves(move)
         
         # If False, the move was invalid
         if checkMove:
            newSet = list(newGame.set)
            chold, dhold = checkMove
            newDep = depth + 1
            expNode += 1

            if tuple(newSet) not in visited:
               visited.add(tuple(checkSet))
               succGen += 1
               genNode += 1
               queue.append((newSet, checkMove,  chold, newDep, f, currentSet))
               cost += chold

      if Flag == 1:
         info += Formatchild(succGen, visited, queue)

def UCS(Start, Goal):
    # Some implemenation are similar to BFS
    info = ""
    visited = {}
    popNode = 0
    expNode = 0
    genNode = 0
            # Re-arranged to fix print output info
    queue = [(0, "Start", 0, Start, 0, None)]
    heapq.heapify(queue)

    while queue:
        #  NEW, checkMove, cost, file, depth, parent [5]
        popNode += 1
        currentCost, move, c, checkSet, depth, parent = heapq.heappop(queue)

        # NEW. Skip if we found a better path already
        Cost = tuple(checkSet)
        if Cost in visited and visited[Cost] <= currentCost:
            continue
        visited[Cost] = currentCost

        if Flag == 1:
            info += "Generating successors to "
            info += FormatQueue(checkSet, move, currentCost, depth, 0, parent)
            
            if expNode % 500 == 0:
               WriteToFile(info)
               info = ""

        if checkSet == Goal:
            parentSet = (currentCost, move, c, checkSet, depth, parent)
            FormatResult(parentSet, checkSet, popNode, expNode, genNode, queue)
            return 1

        succGen = 0
        for move_dir in ["up", "down", "left", "right"]:
            newGame = puzzleGame(checkSet)
            checkMove = newGame.moves(move_dir)

            if checkMove:
                newSet = list(newGame.set)
                key = tuple(newSet)
                
                chold, dhold = checkMove
                newCost = currentCost + chold
                newDepth = depth + 1
                expNode += 1
                
                # NEW. only add if cheaper than existing path
                if newCost < visited.get(key, float('inf')):
                    succGen += 1
                    genNode += 1
                    parentSet = (currentCost, move, c, checkSet, depth, parent)
                    heapq.heappush(queue, (newCost, checkMove, chold, newSet, newDepth, parentSet))

        if Flag == 1:
            info += Formatchild(succGen, visited, queue)

def Greedy(Start, Goal):
   print("Hello greedy")

def A_Star(Start, Goal):
   print("Hello A*")

#3.1 Create the game/rule of the game
""" 
   NOTE:
   Self reminder, Zero would be our perspective/controller 
   even though the other values are being moved.
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
         'down':[-1, 0], 
         'up':[1, 0],
         'right':[0, -1],
         'left':[0, 1]
      }

      # find the offset in a 3x3 array
      posZero_y, posZero_x = divmod(CurrentIndex,3)
      move = moves.get(direction)

      if move:
         newPos_y = posZero_y + move[0]
         newPos_x = posZero_x + move[1]

         # Check if move is within  1D
         if 0 <= newPos_y < 3 and 0 <= newPos_x < 3:
            # Calculate the offset of new index
            newIndex = newPos_y*3 + newPos_x;
            moved = newSet[newIndex]
            # Swap Zero with the moving position and update the Set with new position
            newSet[CurrentIndex], newSet[newIndex] = newSet[newIndex], newSet[CurrentIndex]
            self.set = tuple(newSet)

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
      sys.exit()
   elif  argv[2] != "goal.txt":
      print("Error: Goal file mssing")
      sys.exit()
   
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