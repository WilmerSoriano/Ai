import sys


class compute_posterior:
   # 5 Hypothesis bag
   Hypo = [0.1, 0.2, 0.4, 0.2, 0.1]
   # Where each bag between 0% to 100%
   cherry = [1, 0.75, 0.5, 0.25, 0]
   lime = [0, 0.25, 0.5, 0.75, 1]
   
   def __init__(self, candy, file):
      self.candy = candy
      self.file = file

   def display(self):



if __name__ == "__main__":
   # Extract argument
   arg = sys.argv
   observation = arg[1]
   # Open file
   file = open(" result.txt", 'w')
   file.write("Observation sequence Q: "+observation+"\n")
   file.write("Length of Q: "+str(len(observation)))
   if len(arg) == 1:
      file.write("Before Observations : ???")
   else:
      file.write("Before Observations : ")

   for i in len(observation):
      compute_posterior(observation[i], file)

