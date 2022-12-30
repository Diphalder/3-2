def hill_climbing(graph, start, end):
  current = start
  path = [current]
  global costt

  while (current != end):
    
    if (len(graph[current])==0):
        return None
    dis=0
    

    for adj in graph[current]:
        if(int(dis)<int(costt[(current,adj)])):
            dis=costt[(current,adj)]
            neighbor=adj

    current = neighbor
    path.append(current)
  return path

vertex=[]
graph={}
costt={}

n=int(input("enter number of vertex: "))

for i in range(n):
    x=input()
    if(x not in vertex):
        vertex.append(x)
        graph[x]=[]


n=int(input("enter number of egde: "))
for i in range(n):
    x = input()
    u,v,cost= x.split()
    if(u in vertex and v in vertex):
        graph[u].append(v)
        costt[(u,v)]=cost



start=input("enter start node : ")
end =input("enter end node : ")

print(hill_climbing(graph, start, end)) 

"""
4
A
B
D
C
4
A B 5
A C 10
B D 15
C D 20
"""