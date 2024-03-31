x = int(input("Number x:"))
y  = int(input("Number y:"))

mylist = []
mylist_a = []
mylist01 = []
mylist_p = []

for i in range(1, y + 1):
    if i % x == 0:
        mylist.append(i)
        if i % 2 == 0:
            mylist01.append(0)
        else:
            mylist01.append(1)
for i in mylist[::2]:
    mylist_a.append(i)
for i in mylist[1::2]:
    mylist_p.append(i)

print("Mylist01:", mylist)
print("Mylist01:", mylist01)
print("Mylist_a:", mylist_a)
print("Mylist_p:", mylist_p)