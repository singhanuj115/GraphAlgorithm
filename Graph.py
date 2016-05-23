from Vertex import Vertex

class Graph(object):
   def __init__(self):
       self.vertList = {}
       self.numVertices = 0

   def addVertex(self,key,weight):
       self.numVertices = self.numVertices + 1
       newVertex = Vertex(key,weight)
       self.vertList[key] = newVertex
       return newVertex

   def getVertex(self,n):
       if n in self.vertList:
           return self.vertList[n]
       else:
            return None
   
   def __contains__(self,n):
       return n in self.vertList

   def addEdge(self,main_course,priority_course,cost=0):
       self.vertList[main_course].addNeighbor(self.vertList[priority_course], cost)

   def getVertices(self):
       return self.vertList.keys()

   def __iter__(self):
        return iter(self.vertList.values())               
