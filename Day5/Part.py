import os
def getSize(opcode):
   if (opcode == 1 or opcode ==2):
      return 4
   elif (opcode == 3 or opcode == 4):
      return 2
   elif (opcode == 99):
      return 1
   else:
      print ("Unknown size for opcode {}".format(opcode))
      return 0

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
 #  print ("Instrution, ",opcode) #Debug
 #  print ("Modes ", modes) #Debug
   inputsIndex = list()
   for j in range (1,size):
      if (modes[j-1] == 0):
         inputsIndex.append(Program[i + j])
      else:
         inputsIndex.append(i+j)
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