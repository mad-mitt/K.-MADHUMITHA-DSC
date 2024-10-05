#the bottle shipping problem
def bottles(bottle_count):
    xl=0;l=0;m=0;s=0
    while bottle_count>0:
        if 24<bottle_count:
            xl+=1
            bottle_count-=48
        if 12<bottle_count:
            l+=1
            bottle_count-=24
        if 6<bottle_count:
            m+=1
            bottle_count-=12
        if 0<bottle_count:
            s+=1
            bottle_count-=6
    print("{} xl,{} large,{} medium,{} small".format(xl,l,m,s))
bottle_count=int(input("ENTER BOTTLE COUNT:"))
bottles(bottle_count)


    
        
