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
      nim_misere(red, blue, player)
   else:
      nim_std(red, blue, player)

# For both standard and misere will be in loop until either Zero pile
def nim_std(red, blue, player):

   while red and blue != 0:
      if player == "human":
         red, blue, player = humanTurn(red, blue)
      else:
         red, blue, player = MinMax_AlphaBeta(red, blue)

   print("\n\n\n")
   print("|=*=*=*=*=*=* GAME HAS ENDED! =*=*=*=*=*=*|")
   print("\t      RESULT ARE OUT:\n")
   if red == 0:
      result = blue*3
   else:
      result = red*2
   print(f"\t*{player} has lost: -{result} points!\n")
   if player == "computer":
      print("\t   *HUMAN HAS WON!")
   else:
      print("\t   *COMPUTER HAS WON!")


def nim_misere(red, blue, player):
   
   while red and blue != 0:
      if player == "human":
         red, blue, player = humanTurn(red, blue)
      else:
         red, blue, player = MinMax_AlphaBeta(red, blue)
   print("\n\n\n")
   print("|=*=*=*=*=*=* GAME HAS ENDED! =*=*=*=*=*=*|")
   print("\t      RESULT ARE OUT:\n")
   if red == 0:
      result = blue*3
   else:
      result = red*2
   print(f"\t*{player} has gained: +{result} points!\n")
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

def MinMax_AlphaBeta(red, blue):
   print("\n\n\n")
   print("************* COMPUTER TURN *************")
   print("\n\t\tThinking...")
   #time.sleep(4) # NOTE: this is not necessary... just implementing for aesthetic reason...
   red = 0
   print("\n   ********** END OF TURN ********** ")
   return red, blue, "human"

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