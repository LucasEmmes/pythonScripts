import sys
class a:
    def __init__(self):
        self.c=[0]
        self.p=0
    def i(self):self.c[self.p]=self.c[self.p]+1%256
    def d(self):self.c[self.p]=self.c[self.p]-1%256
    def r(self):
        self.p+=1
        if self.p==len(self.c):self.c.append(0)
    def l(self):
        self.p-=1
        if self.p<0:self.p=0;self.c.insert(0,0)
    def y(self):print(chr(self.c[self.p]),end="")
    def g(self):c=input();self.c[self.p]=(ord(c[0]) if len(c)>0 else 0)%256
    def x(self):return self.c[self.p]
def e(s):
    b=a()
    f=open(s)
    d=f.read()
    f.close()
    i=0
    ls=[]
    lc=0
    while i<len(d):
        c=d[i]
        if c==">":b.r()
        elif c=="<":b.l()
        elif c=="+":b.i()
        elif c=="-":b.d()
        elif c==".":b.y()
        elif c==",":b.g()
        elif c=="[":
            if b.x():ls.append(i-1)
            else:
                lc=1
                while lc!=0:
                    i+=1
                    if d[i]=="[":lc+=1
                    elif d[i]=="]":lc-=1
        elif c=="]":i=ls.pop()
        elif c=="\n":pass
        i+=1
def m():
  if len(sys.argv)==2:e(sys.argv[1])
if __name__=="__main__":m()