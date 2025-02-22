import os
import sys

#3.0 List of available Algorithms
def BFS(Start, Goal, flag):
   print("E")

def UCS(Start, Goal, flag):
   print("Hello UCS")

def Greedy(Start, Goal, flag):
   print("Hello greedy")

def A_Star(Start, Goal, flag):
   print("Hello A*")

#3.1 Create the game/rule of the game in OOP style
""" 
   NOTE:
   Recommed playing 8-puzzle game to
   underatnd rules and mechanics.
"""
class puzzleGame:
   # Grab the initial values from Start.txt
   def __init(self, initialize):
      self.start = initialize

# 2.0 Identify Algorithm
def Algorithms(argv, flag):
   Start = extractNum(argv[1])
   Goal = extractNum(argv[2])

   # If no algorithm inputed, default to A*
   if len(argv) < 4:
      A_Star(Start, Goal, flag)
   else:
      match argv[3]:
         case "bfs":
            BFS(Start, Goal, flag)
         case "ucs":
            UCS(Start, Goal, flag)
         case "greedy":
            Greedy(Start, Goal, flag)
         case "a*":
            A_Star(Start, Goal, flag)

#2.1 Extract the numbers from the file
def extractNum(file):
   numbers = []
   f = open(file, "r")
   for line in f:
      if line != "END OF FILE":
         for num in line.split():
            numbers.append(num)
   f.close()
   return numbers

# 1. Check all user arguments 
if __name__ == "__main__":
   
   # Catch exception:
   argv = sys.argv
   if  argv[1] != "start.txt":
      print("Error: Start file missing")
      exit -1
   elif  argv[2] != "goal.txt":
      print("Error: Goal file mssing")
      exit -1
   
   # Check if dump-flag was set
   flag = 0
   if len(argv) == 5:
      flag = argv[4]
   
   Algorithms(argv, flag)