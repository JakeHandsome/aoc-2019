import os

f = open("{}\\Input.txt".format(os.path.dirname(os.path.realpath(__file__))),"r")
original = f.read().split(",")

for i in range(0, len(original)): 
   original[i] = int(original[i]) 

codes = original.copy()
while True:
   for noun in range(100):
      for verb in range (100):
         codes = original.copy()
         codes[1] = noun
         codes[2] = verb

         # Why doesn't python have a way to do C-Style for loops
         i = 0
         while i < len(codes):
            if (codes[i] == 1):
               codes[codes[i+3]] = codes[codes[i+2]] + codes[codes[i+1]]
            elif (codes[i] == 2):
               codes[codes[i+3]] = codes[codes[i+2]] * codes[codes[i+1]]
            elif (codes[i] == 99):
               break
            else:
               print("You fucked up at {}".format(i))
            i += 4

         if (codes[0] == 19690720):
            print (100 * noun + verb)
            exit(0)
   print ("Everything went wrong")   
   exit(1)
