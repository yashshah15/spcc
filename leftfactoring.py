grammar=input("Enter Productions")
l=grammar.split('|')
l1=[]
for i in l:
    temp=i
    for j in range(1,len(i)) :
        t=i[0:j]
        for k in l:
            if k[0:j]==t and temp !=k:
                pass
            else:
                break
            l1.append(t)
l1=set(l1)
l1=list(l1)
l1.sort()
print(l1)
lp=len(l1[len(l1)-1])
res=[]
for i in l:
    if len(i)==lp:
        res.append("e")
    else:
        res.append(i[lp:])
print("A->",l1[len(l1)-1]+"Z")
print("z->",end="")
for i in res:
    print(i+"|",end="")