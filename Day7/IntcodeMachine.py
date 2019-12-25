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

class IntcodeMachine:
   def __init__(self,initialCode):
      self.initialCode = list(initialCode)
      self.memory = list(initialCode)
      self.instructionPointer = 0
      self.finishedExecuting = False
      self.waitingForInput = False
      self.inputQueue = list()
      self.outputQueue = list()
   def reset(self):
      self.instructionPointer = 0
      self.memory = list(self.initialCode)
   def addInput(self,input):
      self.inputQueue.append(input)
      self.waitingForInput = False
   def readOutput(self):
      assert(len(self.outputQueue) > 0)
      return self.outputQueue.pop(0)
   def executeSingleStep(self):
      opcode = self.memory[self.instructionPointer] % 100
      modes = ((self.memory[self.instructionPointer] // 100)   % 10,
               (self.memory[self.instructionPointer] // 1000)  % 10,
               (self.memory[self.instructionPointer] // 10000) % 10)

      size = self.getSize(opcode)
      inputsIndex = list()
      # Convert the input based on the memory/intermediate mode
      for j in range (1,size):
         if (modes[j-1] == 0):
            # This input is in memory mode. Set the index to be the value of the instruction
            inputsIndex.append(self.memory[self.instructionPointer + j])
         else:
            # This input is in immediate mode. Set the index to be the index of the instruction. This will cause the program to read/write to the current memory location
            inputsIndex.append(self.instructionPointer+j)
      #Switch based on opcode intruction
      if (opcode == Opcode.ADD):
         # Input 1 + Input 2 store to Input 3
         self.memory[inputsIndex[2]] = self.memory[inputsIndex[1]] + self.memory[inputsIndex[0]]
      elif(opcode == Opcode.MULT):
         # Input 1 * Input 2 store to Input 3 
         self.memory[inputsIndex[2]] = self.memory[inputsIndex[1]] * self.memory[inputsIndex[0]]
      elif (opcode == Opcode.STDIN):
         if (len(self.inputQueue) == 0):
            self.waitingForInput = True
            return
         else:
            self.memory[inputsIndex[0]] = self.inputQueue.pop(0)
            self.waitingForInput = False
      elif (opcode == Opcode.STDOUT):
         self.outputQueue.append(self.memory[inputsIndex[0]])
      elif (opcode == Opcode.JEQ):
         if (self.memory[inputsIndex[0]] != 0):
            self.instructionPointer = self.memory[inputsIndex[1]] 
            return # dont increment the instruction pointer
      elif (opcode == Opcode.JNQ):
         if (self.memory[inputsIndex[0]] == 0):
            self.instructionPointer = self.memory[inputsIndex[1]]
            return # dont increment the instruction pointer
      elif (opcode == Opcode.LESSTHAN):
         if (self.memory[inputsIndex[0]] < self.memory[inputsIndex[1]]):
            self.memory[inputsIndex[2]] = 1
         else:
            self.memory[inputsIndex[2]] = 0
      elif (opcode == Opcode.EQUALS):
         if (self.memory[inputsIndex[0]] == self.memory[inputsIndex[1]]):
            self.memory[inputsIndex[2]] = 1
         else:
            self.memory[inputsIndex[2]] = 0
      elif (opcode == Opcode.EXIT):
         self.finishedExecuting = True
      else:
         print("You fucked up at {}".format(self.instructionPointer))
      assert(size != 0)
      self.instructionPointer += size
      # Based on the opcode get the size of it
   def getSize(self,opcode):
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