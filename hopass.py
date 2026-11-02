import numpy as np
inp=[1,1,-1,-1]
w=np.outer(inp,inp)
np.fill_diagonal(w,0)
ninp=[1,1,-1,1]
result=ninp
for i in range(5):
  result=np.where(np.dot(result,w)>=0,1,-1)
print("Inital data :",inp,"\nNoisy data : ",ninp,"\nCorrected data : ",result)
