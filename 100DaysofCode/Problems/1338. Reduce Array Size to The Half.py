class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        m = 0
        for i in arr:
            if i not in freq:
                freq[i] = 0
            freq[i]+=1
        
        x = sorted(freq.values())[::-1]
        res = x[0]
        while res<len(arr)//2:
            m+=1
            res +=x[m]
        return m+1