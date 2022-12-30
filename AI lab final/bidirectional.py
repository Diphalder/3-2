import numpy as np

def bidirectional(graph,revgraph, start, end):
  global visit1
  global visit2

  queue_start = [(start, [start])]
  queue_end = [(end, [end])]
  
  while (queue_start and queue_end):
    (u1, path_forward) = queue_start.pop(0)
    

    if visit2[u1]:  
      return path_forward + list(reversed(path_backward))
    
    visit1[u1]=1
    for v in graph[u1]:
      if(visit1[v]==0):
        queue_start.append((v, path_forward + [v]))
    






    (u2, path_backward) = queue_end.pop(0)
    
    if visit1[u2]:  
      return path_forward + list(reversed(path_backward))
    
    visit2[u2]=1
    for v in revgraph[u2]:
      if(visit2[v]==0):
        queue_end.append((v, path_backward + [v]))
  return None
    
vertex=[]
graph={}
revgraph={}
visit1={}
visit2={}


n=int(input("enter number of vertex: "))

for i in range(n):
    x=input()
    if(x not in vertex):
        vertex.append(x)
        graph[x]=[]
        revgraph[x]=[]
        visit1[x]=0
        visit2[x]=0

n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)
        revgraph[v].append(u)


start=input("enter start node : ")
end =input("enter end node : ")

print("BFS sequence =  ",end="")
x=list(bidirectional(graph,revgraph,start,end))

print(x)

"""
7
S
A
B
C
D
E
G
8
S A
S B
S C
A D
A E
A G
B G
C G
"""