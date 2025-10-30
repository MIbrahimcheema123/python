def matchwords(words):
    ctr = 0
    hi = []
    for  i in words :
        if len(i)>1 and i[0] == i[-1]:
            ctr += 1
            hi.append(i)
    print(hi)
    return ctr
count =matchwords(["abc","def","ghi","klm","nop","qrs","tuv","wxyz"])
print(count)