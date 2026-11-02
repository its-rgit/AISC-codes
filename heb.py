x=[1,-1,1]
y=1
iw=[0,0,0]
lr=1
def heb(x,y,lr):
  return [i*y*lr for i in x]
dw=heb(x,y,lr)
nw=[i+j for i,j in zip(iw,dw)]
print("initial weight = ",iw,"\ndw = ",dw,"\nnew weight = ",nw)

