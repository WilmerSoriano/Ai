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

def FormatQueue(State, Move, Cost, depth, N, parent):
   return f"< state = {State}, action = Moved {Move} g(n) = {Cost}, d = {depth}, f(n) = {N}, Parent = Pointer to {parent} >:\n"

def Formatchild(succGen, visited, queue):
   info = ""
   info += f"\t\t{succGen} successors generated\n"
   info += f"\t\tClosed: {list(visited)}\n"
   info += f"\t\tFringe:[\n"
   for state in queue:
      info += "\t\t\t"
      info += FormatQueue(state[3], state[1], state[2], state[4], state[0], state[5])
   info += f"\t\t]\n"
   return info

def FormatResult(currentSet, checkSet, popNode, expNode, genNode, queue, MaxFringe):
   #queue.append((newSet, checkMove,  chold, newDep, 0, currentSet)) REFRENCE
   info = ""
   solutionPath = []
   cost = 0
   # tracing the path back from Goal to Start
   while currentSet is not None:
      solutionPath.append(currentSet)
      currentSet = currentSet[5]
      
   solutionPath.reverse()
   depSolution = len(solutionPath)
   """
   for MoveCost in solutionPath:
      cost += MoveCost[2]
   """
   # only the cost
   if solutionPath:
      cost = solutionPath[-1][2]  
   
   if Flag == 1:
      info += f"Goal has been found {checkSet}\n"
      info += f"Node Popped:{popNode}\n"
      info += f"Node Expanded:{expNode}\n"
      info += f"Node Generated:{genNode}\n"
      info += f"Max Fringe Size: {str(len(queue))}\n"
      info += f"Solution Found at depth {depSolution-1} with cost of {cost}.\n"
      info += "Steps: "
   print("Goal has been found " + str(checkSet))
   print("Node Popped:", popNode)
   print("Node Expanded:", expNode)
   print("Node Generated:", genNode)
   print("Max Fringe Size:", MaxFringe)
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
   queue = [( 0,("Start", None), 0, Start, 0, None)]
   visited = set()
   info = ""
   popNode = 0
   expNode = 0
   genNode = 1
   MaxFringe = 0

   while queue:
      popNode += 1
      currentSet = queue.pop(0)
      f, checkMove, cost, checkSet, depth, parent = currentSet
   
      if checkSet == Goal:
         if Flag == 1:
            WriteToFile(info)
         FormatResult(currentSet, checkSet, popNode, expNode, genNode, queue, MaxFringe)
         return 1
      
      if tuple(checkSet) not in visited:
            visited.add(tuple(checkSet))
            expNode += 1
      
      if Flag == 1:
         info += "Generating successors to " 
         info += FormatQueue(checkSet, checkMove, cost, depth, 0, parent)

         # Clean up the info-string-type, to make progress faster
         if expNode % 500 == 0:
            WriteToFile(info)
            info = ""

      # Generate all possible successors and play the game
      succGen = 0
      for moves in ["up", "down", "left", "right"]:
         newGame = puzzleGame(checkSet)
         checkMove = newGame.moves(moves)
         
         # If False, the move was invalid
         if checkMove:
            newSet = list(newGame.set)
            chold, dhold = checkMove
            newCost = cost + chold
            newDep = depth + 1
            genNode += 1

            if tuple(newSet) not in visited:
               succGen += 1
               #cost += chold
               queue.append((f, checkMove, newCost, newSet, newDep, currentSet))
      
      MaxFringe = max(MaxFringe, len(queue))
      if Flag == 1:
         info += Formatchild(succGen, visited, queue)

def UCS(Start, Goal):
   # Some implemenation are similar to BFS
   info = ""
   visited = {}
   popNode = 0
   expNode = 0
   genNode = 1
   MaxFringe = 0

   # Re-arranged to fix print output info
   queue = [(0, ("Start", None), 0, Start, 0, None)]
   heapq.heapify(queue)

   while queue:
      #  NEW, checkMove, cost, file, depth, parent [5]
      popNode += 1
      currentSet = heapq.heappop(queue)
      currentCost, move, cost, checkSet, depth, parent = currentSet
      key = tuple(checkSet)

      if checkSet == Goal:
         if Flag == 1:
            WriteToFile(info)
         MainSet = currentSet
         FormatResult(MainSet, checkSet, popNode, expNode, genNode, queue, MaxFringe)
         return 1

      if key in visited and visited[key] <= currentCost:
            continue
      visited[key] = currentCost
      expNode += 1

      if Flag == 1:
         info += "Generating successors to "
         info += FormatQueue(checkSet, move, currentCost, depth, 0, parent)
            
         if expNode % 500 == 0:
            WriteToFile(info)
            info = ""

      succGen = 0
      for moves in ["up", "down", "left", "right"]:
         newGame = puzzleGame(checkSet)
         checkMove = newGame.moves(moves)

         if checkMove:
            newSet = list(newGame.set)
                
            chold, dhold = checkMove
            newCost = currentCost + chold
            newDepth = depth + 1
            genNode += 1
                
            if (tuple(newSet) not in visited) or (newCost < visited.get(tuple(newSet), float('inf'))):
               succGen += 1
               parentSet = (newCost, checkMove, newCost, newSet, newDepth, currentSet)
               heapq.heappush(queue, parentSet)
               MaxFringe = max(MaxFringe, len(queue))
      if Flag == 1:
         info += Formatchild(succGen, visited, queue)

# hueristic(n) = estimate of cost from n to the closest goal
"""
   Using the Manhattan distance
   h(n)= Tile can move to any 
   adjacent square + cost = 47
"""
def heuristic(Start, goalPos):
   heur = 0
   # For every number in Start file
   # find it's position, add desire position 
   # and 
   for line, num in enumerate(Start): 
      if num == 0:
         continue
      target_y, target_x = goalPos[num]
      current_y, current_x = divmod(line, 3)
      heur += num * (abs(current_y - target_y) + abs(current_x - target_x))
   return heur

def Greedy(Start, Goal):
   visited = {}
   popNode = 0
   expNode = 0
   genNode = 1
   max_fringe = 0

   #calcualting herustic
   goalPos = { 
      line: divmod(num, 3)
      for num, line in enumerate(Goal)
         if line != 0
   }
   MainHeu = heuristic(Start, goalPos)

   #(heursitic, move, cost, file, depth, parent)
   queue = [(MainHeu, ("Start", None), 0, Start, 0, None)]
   heapq.heapify(queue)
   info = ""

   while queue:
      popNode += 1
      heur, move, cost, state, depth, parent = heapq.heappop(queue)
      key = tuple(state)

      if state == Goal:
         if Flag == 1:
            WriteToFile(info)
         MainSet = (heur, move, cost, state, depth, parent)
         FormatResult(MainSet, state, popNode, expNode, genNode, queue, max_fringe)
         return 1
      
      if key in visited and visited[key] <= cost:
         continue
      visited[key] = cost
      expNode += 1

      if Flag == 1:
         info += "Generating successors to " 
         info += FormatQueue(state, move, cost, depth, heur, parent)
         WriteToFile(info)
         info = ""

      succGen = 0
      for moves in ["up", "down", "left", "right"]:
         newGame = puzzleGame(state)
         checkMove = newGame.moves(moves)

         if checkMove:
            chold, dhold= checkMove
            newSet = list(newGame.set)
            newDepth = depth + 1
            newCost = cost + chold
            new_h = heuristic(newSet, goalPos)

            # If new state is not in closed or new lower cost
            if (tuple(newSet) not in visited) or (newCost < visited.get(tuple(newSet), float('inf'))):
               parentSet = (heur,(chold, dhold), newCost, state, depth, parent)
               heapq.heappush(queue, (new_h, (chold, dhold), newCost, newSet, newDepth, parentSet))
               genNode += 1
               succGen += 1
   
      max_fringe = max(max_fringe, len(queue))
      if Flag == 1:
         info += Formatchild(succGen, visited, queue)

def A_Star(Start, Goal):
   info = ""
   visited = {} 
   popNode = 0
   expNode = 0
   genNode = 1
   max_fringe = 0

   goal_positions = { 
      line: divmod(num, 3) 
      for num, line in enumerate(Goal) 
         if line != 0
   }
   initial_h = heuristic(Start, goal_positions)

    # (f(n) = g(n) + h(n), move, cost, state, depth, parent)
   queue = [(initial_h + 0, ("Start",None), 0, Start, 0, None)]
   heapq.heapify(queue)

   while queue:
      f, move, g, state, depth, parent = heapq.heappop(queue)
      popNode += 1
      state_key = tuple(state)

      if state == Goal:
         if Flag == 1:
            WriteToFile(info)
         mainState = (f, move, g, state, depth, parent)
         FormatResult(mainState, state, popNode, expNode, genNode, queue, max_fringe)
         return 1
      
      if state_key in visited and visited[state_key] <= g:
         continue
      visited[state_key] = g  # Update the cost to reach this state
      expNode += 1

      if Flag == 1:
         info += "Generating successors to "
         info += FormatQueue(state, move, g, depth, f, parent)
         WriteToFile(info)
         info = ""


      succGen = 0
      for direction in ["up", "down", "left", "right"]:
         game = puzzleGame(state)
         result = game.moves(direction)

         if result:
            moved_tile, dhold = result
            new_state = list(game.set)
            new_g = g + moved_tile
            new_h = heuristic(new_state, goal_positions)
            new_f = new_g + new_h

            # Only add if the state hasn't been visited or the new cost is lower
            if (tuple(new_state) not in visited) or (new_g < visited.get(tuple(new_state), float('inf'))):
               parentSet = (f, (moved_tile, dhold), g, state, depth, parent)
               heapq.heappush(queue, (new_f, (moved_tile, dhold), new_g, new_state, depth + 1, parentSet))
               genNode += 1
               succGen += 1
      max_fringe = max(max_fringe, len(queue))
      if Flag == 1:
         info += Formatchild(succGen, visited, queue)

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