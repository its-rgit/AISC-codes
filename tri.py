def tri(a,b,c,x):
  if x<=b and x>=a:
    return (x-a)/(b-a)
  elif x<=c and x>=b:
    return (c-x)/(c-b)
  else:
    return 0
a,b,c=2,5,8
xtest=[1,3.5,5,6.5,9]
print(" Trianglular function a=2 b=5 c=8")
for i in xtest:
  print("input x = ",i," Memeber ship degree = ",f"{tri(a,b,c,i):.2f}")
