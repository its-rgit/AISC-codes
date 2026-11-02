import random
c=8
mr=0.2
parent1=[random.randint(0,1) for i in range(c)]
parent2=[random.randint(0,1) for i in range(c)]
split=random.randint(0,c-1)
cc=parent1[:split]+parent2[split:]
mc=[i if random.random()>mr else 1-i for i in cc]
print("Parent 1 : ",parent1,"\nParent 2 : ",parent2,"\nCrossover Child split at",split," : ",cc,"\nMutated Child : ",mc)
