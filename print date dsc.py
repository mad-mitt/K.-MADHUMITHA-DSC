#print the date based on the entered day and year
from datetime import datetime, timedelta

month={1:"January",2:"February",3:"March",4:"April",5:"May",6:'June',7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

def Date(y,d):
    start = datetime(y, 1, 1)
    end = start + timedelta(days=d - 1)
    ed= end.strftime('%d-%m-%Y')
    date=ed[:2]+' '+month[int(ed[3:5])]+' '_+ed[6:]
    return date


d=int(input("DATE NUMBER:"))
y=int(input("YEAR:"))
print(Date(y,d))
