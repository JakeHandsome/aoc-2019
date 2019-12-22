import os
f = open("{}\\Input.txt".format(os.path.dirname(os.path.realpath(__file__))),"r")
inputs = f.readline().split("-")

passwords = list()
for x in range (int(inputs[0]),int(inputs[1])):
   stringx = str(x)
   if (
      # Always increaseding
      (int(stringx[0]) <= int(stringx[1]) and 
       int(stringx[1]) <= int(stringx[2]) and 
       int(stringx[2]) <= int(stringx[3]) and 
       int(stringx[3]) <= int(stringx[4]) and 
       int(stringx[4]) <= int(stringx[5])) 
      and
      # Two adjacent numbers
      (stringx[0] == stringx[1] or
      stringx[1] == stringx[2] or
      stringx[2] == stringx[3] or
      stringx[3] == stringx[4] or
      stringx[4] == stringx[5] )):
      passwords.append(x)

print("Part1: {}".format(len(passwords)))