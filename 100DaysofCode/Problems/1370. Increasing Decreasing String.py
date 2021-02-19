
def sortString(self, s: str) -> str:
    res = ''
    ex = {}
    for i in s:
        if i not in ex:
            ex[i] = 0
        ex[i]+=1
    
    while True:
        sort = sorted(ex.keys())
        for i in sort:
            res +=i
            ex[i]-=1
            if ex[i]==0:
                del ex[i]
        if len(ex) == 0:break
        sort = sorted(ex.keys())[::-1]
        for i in sort:
            res +=i
            ex[i]-=1
            if ex[i]==0:
                del ex[i]
        if len(ex) == 0:break
    return res



