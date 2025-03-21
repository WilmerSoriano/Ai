import sys

"""
   NOTE:

   Red marbel = 2 points each
   Blue marbel = 3 points each

   if std version then they are - points
   if misere then they are  points

   Algorithm: MinMax with Alpha Beta Pruning
"""

# [num of Red] [num of Blue] [game version] [human or computer]
def nim(red, blue, version, player):
   print(red, blue, version, player)

#Build the game, build the agent, Micro SD then build the Algorithm.

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