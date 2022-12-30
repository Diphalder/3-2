import numpy as np

from queue import PriorityQueue
q=PriorityQueue()
par={}
def bfs(u,ed):
    global visit
    global graph
    global costt
    global totalcost
    global q
    global pathcost
    global heuristic
    fn=int(heuristic[u])+0
    q.put((fn,u))
    totalcost[u]=0
    while(q.empty!=1):
        h,u=q.get()
        print(u,end=",")
        if(u==ed):
            pathcost=min(pathcost,totalcost[u])
            return
        for v in graph[u]:
            cost=costt[(u,v)]
            par[v]=u
            totalcost[v]=min(totalcost[u]+int(cost),totalcost[v])
            q.put((int(heuristic[v])+totalcost[v],v))
    
vertex=[]
graph={}
totalcost={}
costt={}
heuristic ={}
pathcost=100000000000000

n=int(input("enter number of vertex: "))

for i in range(n):
    z=input()
    x,h= z.split()
    if(x not in vertex):
        vertex.append(x)
        heuristic[x]=h
        graph[x]=[]
        totalcost[x]=100000000000000
        par[x]=None


n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v,cost= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)
        costt[(u,v)]=cost



start=input("enter start node : ")
end =input("enter end node : ")

#print(graph)

print("A-star search sequence = [ ",end="")
bfs(start,end)
print(" ] ")

print("path cost = ", pathcost)


v=end
path=[]
while v is not None:
    path.append(v)
    v=par[v]
path.reverse()
print("the path is = ",  path)


"""
7
S 8 
A 8
B 4
C 3
D 1000000
E 1000000
G 0
8 
S A 1
S B 5
S C 8
A D 3
A E 7
A G 9
B G 4
C G 5
"""
"""
7
S 6
A 0
C 4
G 0
B 6
D 1
E 10
9
S A 2
A C 2
C G 4
S B 1
B E 4
B D 2
A D 3
S G 9
A D 3

"""

"""
7
s 5
a 3
c 3
e 2
g 0
b 4
d 1
7
s a 2
s b 2
b d 2
d g 1
a c 1
c e 1
e g 3
"""