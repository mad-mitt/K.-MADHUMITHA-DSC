#remove duplicates from array
def del_duplicates():
    l=eval(input("ENTER LIST:"))
    for k in l:
        if l.count(k)>1:
            l.remove(k)
    print(l)
del_duplicates()
