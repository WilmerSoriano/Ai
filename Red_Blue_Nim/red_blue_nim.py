import sys


# [num of Red] [num of Blue] [game version] [human or computer]
def nim(red, blue, version, player):
   print(red, blue, version, player)

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