adict = {}
flag = True

s = input("Give alphanumeric value:")
if len(s) == 1:
    print("Μηκος = 1")
else:
    for i in range (len(s) // 2):
        if s[i] != s[- (i + 1)]:
            flag = False
            break
    if flag == True:
        alist = list(s)
        adict[s] = len(s)
        print(adict)
        print(alist)
    else:
        print("This is not a palindrome")