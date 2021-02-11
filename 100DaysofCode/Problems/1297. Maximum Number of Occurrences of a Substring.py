import collections
def getMaxOccur(c,minL,maxL,maxU):
    C = collections.defaultdict(int)
    for i in range(len(c)-minL+1):
        if len(set(c[i:i+minL])) <= maxU:
            C[c[i:i+minL]]+=1
    return max(C.values()) if C else 0