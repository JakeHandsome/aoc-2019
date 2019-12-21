import os
import math

def addFuel(amount):
   fuel = math.floor(int(amount) / 3) - 2
   if (fuel >= 0):
      return fuel + addFuel(fuel)
   else :
      return 0

f = open("{}\\Input.txt".format(os.path.dirname(os.path.realpath(__file__))),"r")
answer = 0
for x in f:
   answer += addFuel(x)
print(answer)

