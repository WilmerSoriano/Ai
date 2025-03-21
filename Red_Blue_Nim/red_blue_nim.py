import sys

"""
   NOTE:   
   
   Points:
   Red marbel = 2 points each
   Blue marbel = 3 points each
   if std version then they are (-) points (Bad)
   if misere then they are (+) points (Good)

   Algorithm: 
   MinMax with Alpha Beta Pruning for Agent player
   (aka: the computer)

   Game:
   When Either player (Computer and Human) is their return,
   they're allow to pick 1 or 2 marble from the pile.

   End-Game:
   When either pile (Red or Blue Marble) is empty 
   (with Zero remaining) the remain marble become the
   points (Either good or bad) each. 
"""
# Select the game version
def settingUp(red, blue, version, player):
   print(red, blue, version, player+ "\n")

   if version == "misere":
      nim_misere(red, blue, player)
   else:
      nim_std(red, blue, player)

def nim_std(red, blue, player):
   print("standard BEGIN"+ "\n")

   while red and blue != 0:
      if player == "human":
         red, blue, player = humanTurn(red, blue)
      else:
         red, blue, player = MinMax_AlphaBeta(red, blue)
      print("in loop")

   print("is out, result:", red, blue)

def nim_misere(red, blue, player):
   print("misere BEGIN"+ "\n")

def humanTurn(red, blue):
   print(red, blue, " My turn!!")
   red = 0
   blue = 56
   return red, blue, "computer"

def MinMax_AlphaBeta(red, blue):
   print(red, blue, " Computer TURN")
   red = 0
   blue = 900
   return red, blue, "human"

#Build the game, build the agent, Micro SD then build the Algorithm

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