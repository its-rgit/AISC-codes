def mcpit(x,w,t):
  y=0  
  for i,j in zip(x,w):
    y+=i*j
  if y>=t:
    return 1
  else:
    return 0
x=[(1,1),(1,0),(0,1),(0,0)]
w=(1,1)
ort=1
andt=2
print("Or Gate \nthreshold : ",ort)
for i in x:
  print("Input : ",i," Output",mcpit(i,w,ort))
print("And Gate \nthreshold : ",andt)
for i in x:
  print("Input : ",i," Output",mcpit(i,w,andt))
  
