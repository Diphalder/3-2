import numpy as np

def dfs(u):
    print(u,end="->")
    global visit
    global graph
    visit[u]=1
    for v in graph[u]:
        if(visit[v]==0):
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

n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)


start=vertex[0]

print("DFS sequence = [ ",end="")
dfs(start)
print(" ] ")









