import os
import itertools
from enum import IntEnum

class Opcode(IntEnum):
   ADD      = 1
   MULT     = 2
   STDIN    = 3
   STDOUT   = 4
   JEQ      = 5 
   JNQ      = 6
   LESSTHAN = 7
   EQUALS   = 8
   EXIT     = 99 

# Based on the opcode get the size of it
def getSize(opcode):
   if (opcode == Opcode.ADD or  
       opcode == Opcode.MULT or
       opcode == Opcode.LESSTHAN or
       opcode == Opcode.EQUALS):
      return 4
   elif (opcode == Opcode.JEQ or
         opcode == Opcode.JNQ):
      return 3
   elif (opcode == Opcode.STDIN or 
         opcode == Opcode.STDOUT):
      return 2
   elif (opcode == Opcode.EXIT):
      return 1
   else:
      print ("Unknown size for opcode {}".format(opcode))
      exit(1)

f = open("{}{}Input.txt".format(os.path.dirname(os.path.realpath(__file__)),os.path.sep),"r")
Init = f.read().split(",")
for i in range(len(Init)): 
   Init[i] = int(Init[i]) 
def mainFunc(inputs):
   Program = list(Init)

   i = 0
   while (i < len(Program)):
      opcode = Program[i] % 100
      modes = ((Program[i] // 100)   % 10,
               (Program[i] // 1000)  % 10,
               (Program[i] // 10000) % 10)

      size = getSize(opcode)
      inputsIndex = list()
      # Convert the input based on the memory/intermediate mode
      for j in range (1,size):
         if (modes[j-1] == 0):
            # This input is in memory mode. Set the index to be the value of the instruction
            inputsIndex.append(Program[i + j])
         else:
            # This input is in immediate mode. Set the index to be the index of the instruction. This will cause the program to read/write to the current memory location
            inputsIndex.append(i+j)
      #Switch based on opcode intruction
      if (opcode == Opcode.ADD):
         # Input 1 + Input 2 store to Input 3
         Program[inputsIndex[2]] = Program[inputsIndex[1]] + Program[inputsIndex[0]]
      elif(opcode == Opcode.MULT):
         # Input 1 * Input 2 store to Input 3 
         Program[inputsIndex[2]] = Program[inputsIndex[1]] * Program[inputsIndex[0]]
      elif (opcode == Opcode.STDIN):
#         Program[inputsIndex[0]] = int(input("Enter Input: "))
         Program[inputsIndex[0]] = inputs.pop(0)
      elif (opcode == Opcode.STDOUT):
         #print (Program[inputsIndex[0]])
         return Program[inputsIndex[0]]
      elif (opcode == Opcode.JEQ):
         if (Program[inputsIndex[0]] != 0):
            i = Program[inputsIndex[1]] 
            continue 
      elif (opcode == Opcode.JNQ):
         if (Program[inputsIndex[0]] == 0):
            i = Program[inputsIndex[1]]
            continue
      elif (opcode == Opcode.LESSTHAN):
         if (Program[inputsIndex[0]] < Program[inputsIndex[1]]):
            Program[inputsIndex[2]] = 1
         else:
            Program[inputsIndex[2]] = 0
      elif (opcode == Opcode.EQUALS):
         if (Program[inputsIndex[0]] == Program[inputsIndex[1]]):
            Program[inputsIndex[2]] = 1
         else:
            Program[inputsIndex[2]] = 0
      elif (opcode == Opcode.EXIT):
         break;
      else:
         print("You fucked up at {}".format(i))
      assert(size != 0)
      i += size

results = list()

for x in list(itertools.permutations(range(5))):
   phases = list(x)
   lastInput = 0
   for x in range(len(phases)):
      lastInput = mainFunc([phases.pop(0),lastInput])
   results.append(lastInput)

print(max(results))