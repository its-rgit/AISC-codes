inp=[(1,1),(1,0),(0,1),(0,0)]
out=[1,0,0,0]
w=[0,0]
b=0
lr=0.1
for e in range(10):
  for i,j in zip(inp,out):
    y=sum(m*n for m,n in zip(i,w))+b
    y=1 if y>=0 else 0
    err=j-y
    dw=[lr*err*s for s in i]
    w=[r+s for r,s in zip(w,dw)]
    b+=err*lr
print("trained weight: ",w,"bias: ",b)
for i in inp:
  y=sum(m*n for m,n in zip(i,w))+b
  y=1 if y>=0 else 0
  print("Input : ",i," Output : ",y)
