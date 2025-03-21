import sys

"""
   NOTE:   
   
   Points:
   Red marbel = 2 points each
   Blue marbel = 3 points each
   if std version then they are (-) points (Bad)
   if misere then they are  (+) points (Good)

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

# [num of Red] [num of Blue] [game version] [human or computer] 
def nim(red, blue, version, player):
   print(red, blue, version, player)

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

   nim(argv[1], argv[2], version, player)