import os
from anytree import Node

def getOrbits(node):
   if (node.parent != None):
      return 1 + getOrbits(node.parent)
   else:
      return 0
def getListOrbitNames(node):


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
