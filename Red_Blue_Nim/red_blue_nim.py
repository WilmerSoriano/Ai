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

# For both standard and misere, will be in loop until either pile is Zero
def nim_game(red, blue, player, version):
   
   while red and blue != 0:
      if player == "human":
         red, blue, player = humanTurn(red, blue)
      else:
         options = possibleMoves(red, blue, version)
         red, blue, player = computerTurn(red, blue, options, version)

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
   print("Human it is your turn, here is your Pile:")
   print(f"\n\t     Red:{red} | Blue:{blue}\n")
   color = input("*Pick a color(red or blue): ")
   
   num = int(input("*How many would you like to remove?(2 or 1): "))
   if color == "red":
      red = red - num
   else:
      blue = blue - num
   print("\n   ========== END OF TURN ========== ")

   return red, blue, "computer"

def computerTurn(red, blue, options, version):
   print("\n\n\n")
   print("************* COMPUTER TURN *************")
   print("\n\t\tThinking...\n")

   alpha = MIN
   beta = MAX
   BestResult = MIN
   BestChoice = None

   # Will always check all 4 options before deciding on best move
   for choice in options:
      newRed = red
      newBlue = blue
      num, color = choice

      if color == "red":
         newRed = num
      else:
         newBlue = num

      result = MinMax_AlphaBeta(newRed, newBlue, alpha, beta, version, False)
      
      # Determine if the result is good or bad option.
      if result > BestResult:
         BestResult = result
         BestChoice = choice
         alpha = max(alpha, BestResult)

   if BestChoice:
      num, color = BestChoice
      if color == "red":
         rem = red - num
         red = num
      else:
         rem = blue - num
         blue = num
      print(f" *Computer removed {rem} from {color} pile")
   print("\n   ********** END OF TURN ********** ")
   return red, blue, "human"

# NOTE to Self: use is_Max/is_Min? to determine MAX or MIN turn
def MinMax_AlphaBeta(red, blue, alpha, beta, version, is_Max):

    # Terminal condition, check both and retreat the score
   if red == 0 or blue == 0:
      score = 2 * red + 3 * blue

      # Standard version
      if version == 0:
         if is_Max:
            return -score  # Computer loses, alert don't take this move
         else:
            return score  # Human loses, then Computer wins, take this move
      # Misere, vise-versa
      else:
         if is_Max:
            return score 
         else:
            return -score 
   
   options = possibleMoves(red, blue, version)

   # Will check if its MAX Turn or MIN Turn (is_Max = Computer Turn, is_Min = Human)
   if is_Max:
      best = MIN
      for choice in options:
         newRed = red
         newBlue = blue
         num, color = choice
         
         if color == "red":
            newRed = num
         else:
            newBlue = num
         
         val = MinMax_AlphaBeta(newRed, newBlue, alpha, beta, version, False)
         
         best = max(best, val)
         alpha = max(alpha, best)
         
         # Prune
         if beta <= alpha:
            break
      return best
   
   # Is is Min turn?
   else: 
      best = MAX
      for choice in options:
         newRed = red
         newBlue = blue
         num, color = choice
         
         if color == "red":
            newRed = num
         else:
            newBlue = num

         val = MinMax_AlphaBeta(newRed, newBlue, alpha, beta, version, True)
         
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