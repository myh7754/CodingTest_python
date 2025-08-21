
n = int(input())
graph = []
for i in range(n):
    k = list(map(int,input()))
    graph.append(k)
count = []
cnt = 0
def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n or graph[y][x]==0:
        return 0
    graph[y][x]= 0
    return 1 + dfs(x,y-1) + dfs(x-1,y) + dfs(x+1,y) + dfs(x,y+1)
  
for i in range(n):
    for j in range(n):
        if graph[j][i] == 1:
            cnt = dfs(i,j)
            count.append(cnt)
            
            
count.sort()
print(len(count))
for i in count:
    print(i)
