text = "man bugun maktabga keldim va o'qishni boshladim va yaxshi baxolar oldim"
new = text.split(" ")
# print(new)
string=new[1:-1]
for n in string:
    print(n,end=' ')
#
s=0
for m in new:
   s+=1
print("\n",s,"ta so'z bor asl ro'yxatta ")