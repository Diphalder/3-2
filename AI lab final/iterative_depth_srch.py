import numpy as np


def dfs(u,goal,depth,par):
  
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
            par[v]=u
            dfs(v,goal,depth,par)
    
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

    par={}
    for v in vertex:
        visit[v]=0
        par[v]=None
    dfs(start,end,depth,par)
    print(" ] ")
    if(srchcomplete):
        v=end
        path=[]
        while v is not None:
            path.append(v)
            v=par[v]
        path.reverse()
        print("the path is = ",  path)
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