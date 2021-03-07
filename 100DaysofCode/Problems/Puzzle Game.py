#  House Robber Algorithm Style
def maxPoints(elements):
    if not elements:
        return 0
    freq = [0]*(max(elements)+1)
    for i in elements:
        freq[i] += i
    DP = [0]*len(freq)
    DP[1] = freq[1]
    for j in range(2,len(freq)):
        DP[j] = max(freq[j]+DP[j-2],DP[j-1])
    return DP[len(freq)-1]