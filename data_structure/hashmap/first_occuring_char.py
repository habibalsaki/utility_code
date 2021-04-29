def hashtable(mylist):
    mydict = {}
    for i in range(len(mylist)):
        if mylist[i] in mydict:
            return mylist[i] 
        else:
            mydict[mylist[i]] = i
    return 0

mylist = [2,1,1,2,3,4,5]
x = hashtable(mylist)
print(x)
