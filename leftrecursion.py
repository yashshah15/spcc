prod=input("Enter Productions")
l=prod.split("|")
t=input("Enter terminal")
c=0
for i in l:
    if i[0]==t:
        c=c+1
for i in range(c,len(l)):
    l[i]=l[i]+t+"'"
print(t+"->",end="")
for i in range(c,len(l)):
    print(l[i]+"|",end="")
print("")
print(t+"'->",end="")
for i in range(0,c):
    print(l[i]+t+"'|",end="")
print("e")
