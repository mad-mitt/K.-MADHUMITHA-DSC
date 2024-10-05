
#Arrange words in a string in the order of their length
def asc_str():
    string=input("ENTER STRING:").lower().split()
    s = sorted(string, key=len)
    return ' '.join(s)

print(asc_str())


