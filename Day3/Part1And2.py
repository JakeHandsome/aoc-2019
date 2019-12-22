# I hate trying to figure out 2D space in my brain.

import os

# Easy function to parse direction and distance and return a point
def drawWire(Wire):
   Points = list()
   X = 0
   Y = 0
   for line in Wire:
      direction = line[0:1]
      distance = int(line[1:len(line)])
      if (direction == "U"):
         Y += distance
      elif (direction == "D"):
         Y -= distance
      elif (direction == "R"):
         X += distance
      else:
         assert(direction == "L")
         X -= distance
      Points.append( (X,Y,distance) )
   return Points

# This is a simple algorithm to determine instersections
# This assumes the line is either horizontal or vertical
# If Line A has constant X and B has constant Y, If the X coord of A is between the two X coords of B AND
#    The Y coord of B is between to the two Y coords of A then they instersect at (A[x],B[y]). Otherwise they do not touch
def findIntersection(A1,A2,B1,B2):
   # A has constant X, B has constant Y
   if (A1[0] == A2[0] and B1[1] == B2[1]):
      if ((A1[0] > min(B1[0],B2[0]) and A1[0] < max(B1[0],B2[0])) and
          (B1[1] > min(A1[1],A2[1]) and B1[1] < max(A1[1],A2[1]))  ):
         return (A1[0],B1[1])
   #A has constant Y, B has constant X
   elif (A1[1] == A2[1] and B1[0] == B2[0]):
      if ((B1[0] > min(A1[0],A2[0]) and B1[0] < max(A1[0],A2[0])) and
          (A1[1] > min(B1[1],B2[1]) and A1[1] < max(B1[1],B2[1]))  ):
         return (B1[0],A1[1])
   #parallel
   else:
      return False
   # Not parallel but not intersecting
   return False


f = open("{}\\Input.txt".format(os.path.dirname(os.path.realpath(__file__))),"r")
Wire1 = f.readline().split(",")
Wire2 = f.readline().split(",")

# Get the points of my wire
Wire1Points = drawWire(Wire1)
Wire2Points = drawWire(Wire2)

manhattenDistancesFromCenter = list()
wireDistancesFromCenter = list()

# Go through each pair of points in order they were drawn.
# Save all the manhatten distances from (0,0)
for i in range(len(Wire1Points)-1):
   for j in range(len(Wire2Points)-1):
      doIntersect = findIntersection(Wire1Points[i],Wire1Points[i+1],Wire2Points[j],Wire2Points[j+1])
      if (doIntersect):
         manhattenDistancesFromCenter.append(sum(doIntersect))
         # The WireXPoints keep track of distance from last point in the [2] index. Sum all those indexes up to this point and add the distance to the instersect point
         wire1distance = sum(x[2] for x in Wire1Points[0:i+1]) + max(abs(doIntersect[0]-Wire1Points[i][0]),abs(doIntersect[1]-Wire1Points[i][1]))
         wire2distance = sum(x[2] for x in Wire2Points[0:j+1]) + max(abs(doIntersect[0]-Wire2Points[j][0]),abs(doIntersect[1]-Wire2Points[j][1]))
         wireDistancesFromCenter.append(wire1distance+wire2distance)
# Print the smallest distance
print("Part1:{}".format(min(manhattenDistancesFromCenter)))
print("Part2:{}".format(min(wireDistancesFromCenter)))