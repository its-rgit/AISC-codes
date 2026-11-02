def trap(a,b,c,d,x):
  if x<=c and x>=b:
    return 1
  elif x<=b and x>=a:
    return (x-a)/(b-a)
  elif x<=d and x>=c:
    return (d-x)/(d-c)
  else:
    return 0
a,b,c,d=1,3,6,8
xtest=[0,2,4.5,7,9]
print(" Trapeazoidal function a=1 b=3 c=6 d=8")
for i in xtest:
  print("input x = ",i," Memeber ship degree = ",f"{trap(a,b,c,d,i):.2f}")
