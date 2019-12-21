import os
import math

f = open("{}\\Input.txt".format(os.path.dirname(os.path.realpath(__file__))),"r")
answer = 0
for x in f:
   answer += math.floor(int(x) / 3) - 2
print(answer)