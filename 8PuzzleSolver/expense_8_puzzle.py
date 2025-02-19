import os
import sys


# 3rd. List of available Algorithms
def BFS(file1num, file2num, flag):
   print(str(file1num[0]) + " Hello BFS " + str(flag))

def UCS(file1num, file2num, flag):
   print("Hello UCS")

def Greedy(file1num, file2num, flag):
   print("Hello greedy")

def A_Star(file1num, file2num, flag):
   print("Hello A*")

# 2nd. Identify Algorithm
def Algorithms(argv, flag):
   file1num = openfile(argv[1])
   file2num = openfile(argv[2])

   # If no algorithm inputed, default to A*
   if len(argv) < 4:
      A_Star(file1num, file2num, flag)
   else:
      match argv[3]:
         case "bfs":
            BFS(file1num, file2num, flag)
         case "ucs":
            UCS(file1num, file2num, flag)
         case "greedy":
            Greedy(file1num, file2num, flag)
         case "a*":
            A_Star(file1num, file2num, flag)

def openfile(file):
   num = []
   f = open(file, "r")
   for line in f:
      if line != "END OF FILE":
         num.append(line)
   f.close()
   return num

# 1st. Check all user arguments 
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