n=int(input())
for i in range(n):
    s=input()
    l=len(s)
    str1,str2="",""
    for i in range(l):
        if i%2==0:
            str1+=s[i]
        else:
            str2+=s[i]
    print(str1+" "+str2)
            
