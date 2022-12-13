n=int(input("n!:"))
s=1
for m in range(1,n+1):
   s*=m
print(s)


d=0
for n in [1,2,5,5,6,4,4,40,10,445,5,2]:
    if n%2==0:
        d+=1
        print(n,end=" ")
print(f"\n{d} ta juft son bor ekan")