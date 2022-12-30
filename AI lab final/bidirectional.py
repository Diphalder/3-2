import numpy as np

def bidirectional(graph, start, end):
  # Create two sets for storing visited nodes
  visited_start = set()
  visited_end = set()
  
  # Create two queues for storing the paths
  queue_start = [(start, [start])]
  queue_end = [(end, [end])]
  
  # Loop until one of the queues is empty
  while queue_start and queue_end:
    # Get the first node from the start queue
    (vertex_start, path_start) = queue_start.pop(0)
    
    # Check if this node has been visited by the other queue
    if vertex_start in visited_end:
      return path_start + list(reversed(path_end))
    
    # Mark the node as visited and add its neighbors to the queue
    visited_start.add(vertex_start)
    for neighbor in graph[vertex_start]:
      if neighbor not in visited_start:
        queue_start.append((neighbor, path_start + [neighbor]))
    
    # Get the first node from the end queue
    (vertex_end, path_end) = queue_end.pop(0)
    
    # Check if this node has been visited by the other queue
    if vertex_end in visited_start:
      return path_end + list(reversed(path_start))
    
    # Mark the node as visited and add its neighbors to the queue
    visited_end.add(vertex_end)
    for neighbor in graph[vertex_end]:
      if neighbor not in visited_end:
        queue_end.append((neighbor, path_end + [neighbor]))
  return None
    
vertex=[]
graph={}

n=int(input("enter number of vertex: "))

for i in range(n):
    x=input()
    if(x not in vertex):
        vertex.append(x)
        graph[x]=[]

n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)


start=input("enter start node : ")
end =input("enter end node : ")

print("BFS sequence = [ ",end="")
bidirectional(graph,start,end)
print(" ] ")

"""
7
S
A
B
C
D
E
G
16
S A
A S
S B
B S
S C
C S
A D
D A
A E
E A
A G
G A
B G
G B
C G
G C
"""