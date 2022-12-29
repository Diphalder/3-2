import numpy as np

def dfs(u,goal,depth):
  
    global visit
    global graph
    global nodedepth
    global srchcomplete
    if(srchcomplete):
        return
    print(u,end=",")
    visit[u]=1
    if(u==goal):
        srchcomplete=1
    for v in graph[u]:
        if(visit[v]==0 and nodedepth[u]+1<=depth):
            nodedepth[v]=nodedepth[u]+1
            dfs(v,goal,depth)
    
vertex=[]
graph={}
visit={}
nodedepth={}


srchcomplete=0

n=int(input("enter number of vertex: "))

for i in range(n):
    x=input()
    if(x not in vertex):
        vertex.append(x)
        graph[x]=[]
        visit[x]=0
        nodedepth[x]=0

n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)


start=input("enter start node : ")
nodedepth[start]=0
end =input("enter end node : ")



for depth in range(len(vertex)):
    print("\titeration - ",depth)
    print("DFS sequence = [ ",end="")

    for v in vertex:
        visit[v]=0
    dfs(start,end,depth)
    print(" ] ")
    if(srchcomplete):
        break




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