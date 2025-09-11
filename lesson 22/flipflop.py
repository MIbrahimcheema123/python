def flipflop(r):
    e = len(r)-1
    s = 0
    while s < e:
        if r[s]!=r[e]:
            return False
        s += 1
        e -= 1
    return True
r = (100,101,102,103,104,105,106,107,108,109,109,108,107,106,105,104,103,102,101,100)
if (flipflop(r)):
    print ("This is a flipflop")
else:
    print("this is not a flipflop")