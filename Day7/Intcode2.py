import os
import itertools
from IntcodeMachine import IntcodeMachine

f = open("{}{}Input.txt".format(os.path.dirname(os.path.realpath(__file__)),os.path.sep),"r")
Init = f.read().split(",")
for i in range(len(Init)): 
   Init[i] = int(Init[i]) 

results = list()
for phases in list(itertools.permutations(range(5,10))):

   Machines = list()
   for phase in phases:
      icm = IntcodeMachine(Init)
      icm.addInput(phase)
      Machines.append(icm)

   loopy = itertools.cycle(Machines)


   done = False
   buffer = [0]

   while(done == False):
      amp = next(loopy)
      while (len(buffer) > 0):
         amp.addInput(buffer.pop(0))
      while (amp.finishedExecuting == False and amp.waitingForInput == False):
         amp.executeSingleStep()
      while (len (amp.outputQueue) > 0 ) :
         buffer.append(amp.readOutput())
      if (amp.finishedExecuting and amp == Machines[4]): # Make sure this is machine 'E'
         done = True
   results.append(buffer.pop())
print("Part 2:{}".format(max(results)))