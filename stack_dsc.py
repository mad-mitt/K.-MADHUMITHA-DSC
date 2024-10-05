#stack operations
def push():
    x=int(input("ENTER ELEMENT:"))
    L.append(x)
def pop():
    x=L.pop()
    return x
def peek():
    return L[-1]
print('''     MENU
1)ADD ELEMENT TO STACK
2)POP THE LAST ENTERED ELEMENT
3)PEEK
4)EXIT''')

L=[]
ch=int(input("ENTER OPTION:"))
while ch:
    if ch==1:
        push()
        print(L)
        
    elif ch==2:
        if len(L)>0:
            print(pop(),'\n',L)
        else:
            print("EMPTY STACK")
    elif ch==3:
        print(peek())
    elif ch==4:
        print("Exiting!")
        break
    else:
        print("INVALID OPTION! TRY AGAIN")
    ch=int(input("ENTER OPTION:"))

