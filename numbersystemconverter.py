def runner():
    L=[]
    print('''******************************MENU******************************
                1.BINARY NUMBER
                2.OCTAL NUMBER
                3.HEXADECIMAL NUMBER
''')
    z=input("")
    
    if z=='1':
        r=2
    elif z=='2':
        r=8
    elif z=='3':
        r=16
    else:
        print("INVALID INPUT!!")
    

    
    if z=='1' or z=='2' or z=='3':
        n=input("Decimal number:")
    else:
        print("")
    l1=len(n)
    def checker1(n,l):
        L5=['0']
        global m1
        global j1
        global kd
        for i in range(l):
            c=''
            j=''
            if n[i]==".":
                m1=1
                j1=i
                break
            else:
                kd=n
                m1=2
                j1=l+1
    O1=[]
    def floatsolver(n,l):
        def checker(n,l):
            O=[]
            dj=['0']
            global m
            global g
            global j
            global c
            global b
            j=0
            g=0
            c=''
            for i in range(l):
                if n[i]==".":
                    m=1
                    j=i
                    break
                else:
                    j=0
                    m=2
                    g=0
            if m==1:
                for k in range(j,l):
                    O.append(n[k])
                for k1 in O:
                    c+=k1
                g=float(c)
                b=g
            return m,g,j
                
        O=['0']
        checker(n,l1)
        while m<2:
            if b==0:
                break
            else:
                n1=str(r*b)
                l2=len(str(n1))
                O.clear()
                O=[]
                c=''
                checker(str(n1),l2)
                n2=str(n1[0:j])
                if r==16:
                    dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
                    if int(n2)>9:
                        n3=dic.get(int(n2))
                        O1.append(n3)
                    else:
                        O1.append(n2)
                else:
                    O1.append(n2)
                l11=len(O1)
                if l11>(20+len(n)-len(kd)):
                    break
        global c1
        global ht
        c1='.'
        for k2 in O1:
            c1+=k2
        return c1
        
    
    def wholesolver(kd,n,r):
        kd=n[0:j1]
        n=int(kd)
        p=n
        d=''
        h=0
        for j in range(p+1):
            k=pow(r,j)
            if k>p:
                h=j
                break
            else:
                continue
        if n==0:
            L.append(n)
        else:
            if r==2 or r==8:
                for i in range(h):
                    if n==1:
                        b=1
                        L.append(b)
                    else:
                        b=n%r
                        n=n//r    
                        L.append(b)
            if r==16:
                for i in range(h):
                    if n==1:
                        b=1
                        L.append(b)
                    else:
                        b=n%r
                        n=n//r
                        
                        if b>9:
                            G={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
                            f=G.get(b)
                            L.append(f)
                        else:
                            L.append(b)
    l3=len(n)
    d=''
    hg=0
    checker1(n,l3)
    if m1==2:
        wholesolver(kd,n,r)
        hg=''
    if m1==1:
        hg=floatsolver(n,l3)
        wholesolver(kd,n,r)           
    
    for g in L:
        s=g
        d=str(s)+str(d)
    d=d+str(hg)
    if r==2:
        print("Binary Number:",d)
    if r==8:
        print("Octal Number:",d)
    if r==16:
        print("Hexadecimal Numbar:",d)

    print("To use this program again press <1> otherwise press any key:")
    y=input("")
    if y=='1':
        runner()
    else:
        print("Thankyou")
    
runner()
#Aaj 17 February 2022 hai aur ST 2 bhi khtm hue hain aaj jis task ko pura krne ka socha tha woh ho gya..


    
    



