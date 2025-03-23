""" NOTE:   
   * Points:
   Red marbel = 2 points each
   Blue marbel = 3 points each
   if std version then they are (-) points (Bad)
   if misere then they are (+) points (Good)

   * Algorithm: 
   MinMax with Alpha Beta Pruning for Agent player
   (aka: the computer)

   * Game:
   When Either player (Computer and Human) is their return,
   they're allow to pick 1 or 2 marble from the pile.

   * End-Game:
   When either pile (Red or Blue Marble) is empty 
   (with Zero remaining) the remain marble become the
   points (Either good or bad) each. 
"""

import sys
import time

MAX = 1000
MIN = -1000

# Setting up the game version before it starts
def settingUp(red, blue, version, player):
   print("|===============================|")
   print("| Setting up your Nim-Game...\t|")
   print(f"| Pile: {red} marbel and {blue} marbel.|")
   print(f"| Version: {version}\t\t|")
   print(f"| First turn: {player}\t\t|")
   print("|===============================|")

   red = int(red)
   blue = int(blue)

   if version == "misere":
      nim_game(red, blue, player, 1)
   else:
      nim_game(red, blue, player, 0)

# For both standard and misere will be in loop until either Zero pile
def nim_game(red, blue, player, version):
   
   while red and blue != 0:
      if player == "human":
         red, blue, player = humanTurn(red, blue)
      else:
         option = possibleMoves(red, blue, version)
         red, blue, player = computerTurn(red, blue, option, version)

   endGame(red, blue, player, version)

# Generate Valid possible moves
def possibleMoves(red, blue, version):
   # Standard Ver
   option = []
   if version == 0:
      if red >= 2:
         option.append((red - 2, "red"))      
      if blue >= 2:
         option.append((blue - 2, "blue"))
      
      if red >= 1:
         option. append((red - 1, "red"))
      if blue >= 1:
         option.append((blue - 1, "blue"))
   else: # Misere
      if blue >= 1:
         option.append((blue - 1, "blue"))
      if red >= 1:
         option. append((red - 1, "red"))

      if blue >= 2:
         option.append((blue - 2, "blue"))
      if red >= 2:
         option.append((red - 2, "red"))

   return option

def endGame(red, blue, player, version):
   print("\n\n\n")
   print("|=*=*=*=*=*=* GAME HAS ENDED! =*=*=*=*=*=*|")
   print("\t      RESULT ARE OUT:\n")

   # Calculates total points left
   if red == 0:
      result = blue*3
   else:
      result = red*2

   # Determine the correct game (either give +/- points)
   if version == 1:
      print(f"\t*{player} has gained: +{result} points!\n")
   else:
      print(f"\t*{player} has gained: -{result} points!\n")

   # Gives the correct winnig sign to player
   if player == "computer":
      print("\t   *COMPUTER HAS WON!")
   else:
      print("\t   *HUMAN HAS WON!")
  
def humanTurn(red, blue):
   print("\n\n\n")
   print("============= HUMAN TURN =============")
   print("Human it is you turn, here is you Pile:")
   print(f"\n\tRed:{red}\t| Blue:{blue}\n")
   color = input("*Pick a color(red or blue): ")
   
   num = int(input("*How many would you like to remove?(2 or 1): "))
   if color == "red":
      red = red - num
   else:
      blue = blue - num
   print("\n   ========== END OF TURN ========== ")

   return red, blue, "computer"

def computerTurn(red, blue, option, version):
   print("\n\n\n")
   print("************* COMPUTER TURN *************")
   print("\n\t\tThinking...\n")

   alpha = MAX
   beta = MIN
   Bestscore = MIN
   BestState = ""

   for state in option:
      currentRed = red
      currentBlue = blue
      num, color = state
      
      if color == "red":
         currentRed = num
      else:
         currentBlue = num

      result = MinMax_AlphaBeta(currentRed, currentBlue, alpha, beta, version, False)
      
      if result > Bestscore:
         Bestscore = result
         

   # Determine which option the Comp took the set red/blue to that number
   print(f"Computer removed ")

   print("\n   ********** END OF TURN ********** ")
   return red, blue, "human"

def MinMax_AlphaBeta(nodeIndex, maximizingPlayer, state, alpha, beta):

   if :
      return state[nodeIndex]
   if maximizingPlayer: 
      best = MIN
 
      # Recur for left and right children 
      for i in range(0, 2): 
             
         val = MinMax_AlphaBeta(, , False, state, alpha, beta)
         print("Val HERE:", val) 
         best = max(best, val) 
         alpha = max(alpha, best) 
 
         # Alpha Beta Pruning 
         if beta <= alpha: 
            break
      return best 
   
   else:
      best = MAX
 
      # Recur for left and right children 
      for i in range(0, 2): 
         val = MinMax_AlphaBeta(, , True, values, alpha, beta)
         best = min(best, val) 
         beta = min(beta, best) 
 
         # Alpha Beta Pruning 
         if beta <= alpha: 
            break
      return best

# 1. Check all user arguments 
if __name__ == "__main__":

   argv = sys.argv
   if len(argv) > 3:
      version = argv[3]
   else:
      version = "standard"

   if len(argv) > 4:
      player = argv[4]
   else:
      player = "computer"

   # [num of Red] [num of Blue] [game version] [human or computer] 
   settingUp(argv[1], argv[2], version, player)