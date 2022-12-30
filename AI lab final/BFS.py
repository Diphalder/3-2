import numpy as np

q=[]

def bfs(u,end):
    global visit
    global graph
    global par
    q.append(u)
    visit[u]=1
    while(len(q)!=0):
        u=q.pop(0)
        print(u,end=",")
        if(u==end):
            return
        for v in graph[u]:
            if(visit[v]==0):
                q.append(v)
                par[v]=u
                visit[v]=1
    
vertex=[]
graph={}
visit={}
par={}

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

print("BFS sequence = [ ",end="")
bfs(start,end)
print(" ] ")


path=[]

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