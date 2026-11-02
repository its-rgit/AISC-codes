a={"x1":0.2,"x2":0.7,"x3":0.4,"x4":1.0}
b={"x1":0.5,"x2":0.3,"x3":0.9,"x4":0.0}
u={x:max(a[x],b[x]) for x in a}
i={x:min(a[x],b[x]) for x in a}
ca={x:round(1-a[x],1) for x in a}
cb={x:round(1-b[x],1) for x in a}
print("Fuzzy set A",a,"\nFuzzy set B",b,"\nUnion (AUB) ",u,"\nIntersection (AnB) ",i,"\nComplement A ",ca,"\nComplement B ",cb)
