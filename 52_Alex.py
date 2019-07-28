import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for x in range(3,int(n**0.5)+1,2):
        if n%x==0:
            return False
    return True

def isPrime2(n):
    if n in primes_cache:
        return True
    return False

def findFactors(n):
    z=n
    y=z**.5+1
    p=2
    while p<y:
        if z%p==0:
            if not isPrime(p+z/p):
                return False
            #print z, p
        p=p+1
    return True

def main(a):
    total=0
    t=time.time()
    primes=Primes(a)
    for x in range(2,a+1,4):
        if primes[x+1] and primes[x/2+2]:
            if x%4!=0 and x%9!=0:
                sqrt=int(x**.5)+1
                if all(primes[d+x/d] for d in range(3, sqrt) if x%d==0):
                    total+=x
    print total+1, time.time()-t
main(100000000)