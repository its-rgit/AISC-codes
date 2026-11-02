graph={"A":["B","C"],"B":["D","E"],"C":["F"],"D":[],"E":[],"F":[]}
def bfs(st,q):
  if st:
    a=st.pop(0)
    if a not in q:    
      q.append(a)
      st+=graph[a]
    bfs(st,q)
    return q
print("BFS Traversal Order from A is : ",bfs(["A"],[]))
