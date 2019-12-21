import os

f = open("{}\\Input.txt".format(os.path.dirname(os.path.realpath(__file__))),"r")
codes = f.read().split(",")

for i in range(0, len(codes)): 
   codes[i] = int(codes[i]) 

codes[1] = 12
codes[2] = 2
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

print (codes[0])