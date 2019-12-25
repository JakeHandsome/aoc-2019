import os
from anytree import Node
from anytree.search import findall

def getOrbits(node):
   if (node.parent != None):
      return 1 + getOrbits(node.parent)
   else:
      return 0
def findCommonParent(a,b):
   commonParent = a
   while True:
      res = findall(commonParent, filter_=lambda node: node.name == b.name)
      if (commonParent.parent == None):
         return None
      elif (res):
         return commonParent
      commonParent = commonParent.parent
def getDistanceFromParent(node,parent):
   distance = 1
   currentNode = node.parent
   while (currentNode != parent):
      distance += 1
      currentNode = currentNode.parent
   return distance
f = open("{}{}Input.txt".format(os.path.dirname(os.path.realpath(__file__)),os.path.sep),"r")
Input = [line.rstrip() for line in f]

graph = dict()

for line in Input:
   nodes = line.split(')')
   for node in nodes:
      if (node not in graph):
         graph[node] = Node(node)
   graph[nodes[1]].parent = graph[nodes[0]]

# Count how many parents each node has
numberOfOrbits = 0
for n in graph.values():
   numberOfOrbits += getOrbits(n)
print ("Part 1: {}".format(numberOfOrbits))

# I could just use 'Walker' for the second part but I feel like writing my own
commonParent = findCommonParent(graph["YOU"],graph["SAN"])
distance = getDistanceFromParent(graph["YOU"],commonParent) + getDistanceFromParent(graph["SAN"],commonParent) - 2
print ("Part 2: {}".format(distance))