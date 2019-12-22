import os
import re

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
      passwords.append(stringx)

print("Part1: {}".format(len(passwords)))
Part2 = list()
# Check every password we already found
for password in passwords:
   # At minumum we have a 1 digit streak
   streak = 1
   for i in range(len(password)-1):
      # check the current digit against the next. If it matches increment our streak
      if (password[i] == password[i+1]): 
         streak += 1
      # if it doesn't match
      else:
         # and our current streak is 2, stop we found a good password
         if streak == 2 :
            break
         # other wise reset the streak and keep going
         else:
            streak = 1
   # if this password had a streak of 2, keep it
   if streak == 2:
      Part2.append(password)
#answer
print("Part2: {}".format(len(Part2)))