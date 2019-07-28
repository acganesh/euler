import time
def factor(a):
    sieve=[[] for x in range(a+1)]
    for x in range(2,a):
        for y in range(x,a+1,x):
            sieve[y].append(x)
    return sieve

def main(a):
    t=time.time()
    f=factor(a)
    array=[0,0]+[1]*(a-1)
    for x in range(2,a+1):
        for f1 in f[x]:
            for f2 in f[x-1]:
                f3=f1*f2
                if f3>a: break
                if f3>x: array[f3]=x
    print (sum(array), time.time()-t)

def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(int(a/x)-1)
    return sieve

def primeSieve(a):
    sieve=[0 for x in range(a+1)]
    p=Primes(a)
    for x in range(2,a+1):
        if p[x]:
            for y in range(x,a+1,x):
                sieve[y]=x
    return sieve, p

def main2(a):
    t=time.time()
    f,p=primeSieve(a)
    total=0
    for x in range(2,a+1):
        if not p[x]:
            y=f[x]
            z=x-y
            while 1:
                if z*(z+1)%x==0:
                    total+=z+1
                    break
                elif z*(z-1)%x==0:
                    total+=z
                    break
                else:
                    z-=y
        else:
            total+=1
    print (total, time.time()-t)
            
main(10000000)
#main2(10**7)  