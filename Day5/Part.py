import os

# Based on the opcode get the size of it
def getSize(opcode):
   if (opcode == 1 
       or opcode ==2):
      return 4
   elif (opcode == 3 
         or opcode == 4):
      return 2
   elif (opcode == 99):
      return 1
   else:
      print ("Unknown size for opcode {}".format(opcode))
      exit(1)

f = open("{}{}Input.txt".format(os.path.dirname(os.path.realpath(__file__)),os.path.sep),"r")
Program = f.read().split(",")

#Program = "3,0,4,0,99".split(",")

for i in range(len(Program)): 
   Program[i] = int(Program[i]) 
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
   if (opcode == 1):
      # Input 1 + Input 2 store to Input 3
      Program[inputsIndex[2]] = Program[inputsIndex[1]] + Program[inputsIndex[0]]
   elif(opcode == 2):
      # Input 1 * Input 2 store to Input 3 
      Program[inputsIndex[2]] = Program[inputsIndex[1]] * Program[inputsIndex[0]]
   elif (opcode == 3):
      Program[inputsIndex[0]] = int(input("Enter Input: "))
   elif (opcode == 4):
      print (Program[inputsIndex[0]])      
   elif (opcode == 99):
      break;
   else:
      print("You fucked up at {}".format(i))
   assert(size != 0)
   i += size