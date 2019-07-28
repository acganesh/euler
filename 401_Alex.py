import time
def r(k,n):
    return (n*(n+1)*(2*n+1)-(k-1)*(k)*(2*k-1))/6

def add(n,a):
    return int(a/n)*n**2

def main(a):
    t=time.time()
    mi=a/2
    mx=a
    sa=a**.5+1
    total=0
    x=1
    while x<sa:
        mi=a/(x+1)+1
        mx=a/(x)
        total+=(x)*r(mi,mx)
        total+=add(x,a)
        x+=1
        #print x
    if x>mi:
        total-=add(x-1,a)
    print (total)%(10**9), time.time()-t

main(10**13)