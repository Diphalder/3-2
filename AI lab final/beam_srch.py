import numpy as np

from queue import PriorityQueue
q=PriorityQueue()
newQ=PriorityQueue()

par={}
def bfs(u,ed):
    global graph
    global costt
    global totalcost
    global q
    global pathcost
    global heuristic
    global newQ
    global beamsize
    q.put((heuristic[u],u))
    totalcost[u]=0
    while(q.empty!=1):
        h,u=q.get()
        print(u,end=",")
        if(u==ed):
            pathcost=min(pathcost,totalcost[u])
            return
        newQ=q
        q.queue.clear()
        for v in graph[u]:
                cost=costt[(u,v)]
                par[v]=u
                totalcost[v]=min(totalcost[u]+int(cost),totalcost[v])
                newQ.put((heuristic[v],v))
        for i in range(beamsize):
            x=newQ.get()
            q.put(x)
            
    
vertex=[]
graph={}

totalcost={}
costt={}
path=[]
heuristic ={}
beamsize=int(input("enter BEAM size = "));
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

print("BEAM search sequence = [ ",end="")
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
2
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
