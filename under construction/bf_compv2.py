import sys
def e(s):
    (f:=open(s),d:=f.read(),f.close(),i:=0,s:=[],c:=0,p:=0,f:=[0])
    while i<len(d):
        c=d[i]
        if c==">":p+=1;f.append(0)if p==len(f)else 0
        if c=="<":p-=1 if p>0 else f.insert(0,0)
        if c=="+":f[p]=f[p]+1%256
        if c=="-":f[p]=f[p]-1%256
        if c==".":print(chr(f[p]),end="")
        if c==",":e=input();f[p]=(ord(e[0])if len(e)>0 else 0)%256
        if c=="[":
            if f[p]:s.append(i-1)
            else:
                c=1
                while c!=0:
                    i+=1
                    if d[i]=="[":c+=1
                    elif d[i]=="]":c-=1
        if c=="]":i=s.pop()
        i+=1
def m():
    if len(sys.argv)==2:e(sys.argv[1])
if __name__=="__main__":m()