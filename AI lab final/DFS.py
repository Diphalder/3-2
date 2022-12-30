import numpy as np


path=[]
par={}
def dfs(u):
    print(u,end=",")
    global visit
    global graph
    visit[u]=1
    for v in graph[u]:
        if(visit[v]==0):
            par[v]=u
            dfs(v)

    
vertex=[]
graph={}
visit={}

n=int(input("enter number of vertex: "))

for i in range(n):
    x=input()
    if(x not in vertex):
        vertex.append(x)
        graph[x]=[]
        visit[x]=0
        par[x]=None

n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)


start=input("enter start node : ")
end =input("enter end node : ")

print("DFS sequence = [ ",end="")
dfs(start)
print(" ] ")


v=end
path=[]
while v is not None:
    path.append(v)
    v=par[v]
path.reverse()
print("the path is = ",  path)




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




