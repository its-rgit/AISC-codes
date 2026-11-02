graph={"A":[("B",1),("C",4)],"B":[("D",5)],"C":[("D",1)],"D":[]}
h={"A":6,"B":4,"C":1,"D":0}
def search(st,gl):
  q=[]
  q.append((st,h[st],0,[st]))
  while q:
    cr=q.pop(0)
    ap=graph[cr[0]]
    for i in ap:
      if i[0] not in cr[3]: 
        q.append((i[0],h[i[0]],cr[2]+i[1],cr[3]+[i[0]]))
        q=sorted(q,key=lambda x:x[1])
    if cr[3][-1]==gl:
      return (cr[2],cr[3])
  return (-1,"None")
print(search("A","D"))

