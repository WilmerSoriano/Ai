import os

#list of available Algorithms

def BFS():

def UCS():

def Greedy():

#default Algorithm
def A_Star():


#verify file and determine User input
def main(*args):
   #1st catch exception:
   if args[0] != "start.txt":
      print("Error: Start file missing")
      return -1
   elif args[1] != "goal.txt":
      print("Error: Goal file mssing")
      return -1
   