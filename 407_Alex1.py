import itertools
import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def factors(a):
    sieve=[[] for x in range(a+1)]
    for x in range(1,a):
        for y in range(x,a+1,x):
            sieve[y].append(x)
    return sieve

def mul(a):
    t=1
    for x in a:
        t*=x
    return t

def factorSieve2(a):
    p=Primes(a)
    sieve=[[] for x in range(a+1)]
    for x in range(2,a):
        if p[x]:
            for z in range(x, a+1, x):
                sieve[z].append(x)
    return sieve



def factorSieve(a):
    p=Primes(a)
    sieve=[[] for x in range(a+1)]
    for x in range(2,a):
        if p[x]:
            y=x
            while y<a:
                for z in range(y, a+1, y):
                    sieve[z].append(x)
                y*=x
    return sieve

def main2(a):
    t=time.time()
    array=[1]*(a+1)
    f=factorSieve(a)
    for x in range(2,a+1):
        fa=f[x]+f[x-1]
        for y in range(len(fa)):
            for z in itertools.combinations(fa,y):
                #print z
                m=mul(z)
                if m<=a:
                    if m>x:
                        if array[m]<x:
                            array[m]=x
    print sum(array), array
    print time.time()-t

pf=factorSieve2(10**6)
def relPrime(a,b):
    return len([x for x in pf[a] if x in pf[b]])<1

def main(a):
    t=time.time()
    print "starting"
    array=[1]*(a+1)
    array[0]=0
    f=factors(a)
    print "factored", time.time()-t
    for x in range(2,a+1):
        if not len(pf[x])==1:
            for y in range(len(f[x])/2-1,0,-1):
                if relPrime(f[x][y],f[x][(y+1)*-1]):
                    b=f[x][y]
                    c=f[x][(y+1)*-1]
                    tb=b
                    tc=c
                    while tb<tc:
                        tb+=b
                    while tb-tc!=1:
                        tc+=c
                        while tb<tc:
                            tb+=b
                    array[x]=tb
                    break
    print sum(array)
    #print array
    print time.time()-t
                

main(10**7)
#main2(100)