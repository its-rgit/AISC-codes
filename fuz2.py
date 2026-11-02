a={"x1":0.6,"x2":0.4,"x3":0.9}
b={"x1":0.5,"x2":0.2,"x3":0.3}
bsum={k:min(1.0,round(a[k]+b[k],1)) for k in a}
bdiff={k:max(0.0,round(a[k]+b[k]-1,1)) for k in a}
print("Fuzzy Set A : ",a)
print("Fuzzy Set B : ",b)
print("Bounded sum : ",bsum)
print("Bounded difference : ",bdiff)



