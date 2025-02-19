import os
import sys

# List of available Algorithms

def BFS(flag):
   print("Hello BFS" + flag)
def UCS(flag):
   print("Hello UCS")
def Greedy(flag):
   print("Hello greedy")
# Default Algorithm
def A_Star(flag):
   print("Hello A*")


# Verify file and determine User input
def main():
   inputs = sys.argv

   # 1st. Catch exception:
   if  inputs[1] != "start.txt":
      print("Error: Start file missing")
      return -1
   elif  inputs[2] != "goal.txt":
      print("Error: Goal file mssing")
      return -1
   


   # 2nd. Check identify Algorithm
   match inputs[3]:
      case "bfs":
         BFS(inputs[4])
      case "ucs":
         UCS(inputs[4])
      case "greedy":
         Greedy(inputs[4])
      case "a*":
         A_Star(inputs[4])
      case _:
         A_Star(inputs[4])

if __name__ == "__main__":
    main()
