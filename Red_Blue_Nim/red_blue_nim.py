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
   # Misere
   else: 
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
   print(f"\t      Red:{red} | Blue:{blue}\n")

   # Calculates total points left
   result = 2 * red + 3 * blue

   # Determine the correct game (either give +/- points) and gives the correct winnig sign to player
   winner = None
   if version == 1:
      print(f"\t*{player} has gained: +{result} points!\n")
      winner = "\t   *COMPUTER HAS WON!" if player == "computer" else "\t   *HUMAN HAS WON!"
   else:
      print(f"\t*{player} has gained: -{result} points!\n")
      winner = "\t   *HUMAN HAS WON!" if player == "computer" else "\t   *COMPUTER HAS WON!"

   print(winner)
  
def humanTurn(red, blue):
   print("\n\n\n")
   print("============= HUMAN TURN =============")
   print("Human it is you turn, here is you Pile:")
   print(f"\n\t     Red:{red} | Blue:{blue}\n")
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

   alpha = MIN
   beta = MAX
   Bestscore = MIN
   BestState = None

   for state in option:
      newRed = red
      newBlue = blue
      num, color = state

      if color == "red":
         newRed = num
      else:
         newBlue = num

      result = MinMax_AlphaBeta(newRed, newBlue, alpha, beta, version, False)
      
      if result > Bestscore:
         Bestscore = result
         BestState = state
         alpha = max(alpha, Bestscore)
      if beta <= alpha:
         break

   if BestState:
      num, color = BestState
      if color == "red":
         removed = red - num
         red = num
      else:
         removed = blue - num
         blue = num
      print(f" *Computer removed {removed} from {color} pile")

   print("\n   ********** END OF TURN ********** ")
   return red, blue, "human"

def MinMax_AlphaBeta(red, blue, alpha, beta, version, is_max_turn):

    # Terminal condition check
   if red == 0 or blue == 0:
      score = 2 * red + 3 * blue

      if version == 0:  # Standard version
         if is_max_turn:
            return -score  # Computer loses (their turn)
         else:
            return score  # Human loses (computer wins)
      else:  # Misère version
         if is_max_turn:
            return score  # Computer wins (their turn)
         else:
            return -score  # Human wins (computer loses)
   
   moves = possibleMoves(red, blue, version)

   if is_max_turn:
      best = MIN
      for move in moves:
         new_red = red
         new_blue = blue
         num, color = move
         
         if color == "red":
            new_red = num
         else:
            new_blue = num
         
         val = MinMax_AlphaBeta(new_red, new_blue, alpha, beta, version, False)
         
         best = max(best, val)
         alpha = max(alpha, best)
         
         # Prune
         if beta <= alpha:
            break
      return best
   else:
      best = MAX
      for move in moves:
         new_red = red
         new_blue = blue
         num, color = move
         
         if color == "red":
            new_red = num
         else:
            new_blue = num

         val = MinMax_AlphaBeta(new_red, new_blue, alpha, beta, version, True)
         
         best = min(best, val)
         beta = min(beta, best)

         # Prune
         if beta <= alpha:
            break
      return best

#Check all user arguments 
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