n = 5
nums = [1,5]


incr = [0]*(n+2)
for i in range(len(nums)-1):
    start = min(nums[i],nums[i+1])
    end = max(nums[i],nums[i+1])
    incr[start]+=1
    incr[end+1]-=1
    i+=1

scrs = [0]*(n+1)
scr = 0
for j in range(1,n+1):
    scr += incr[j]
    scrs[j] = scr
    j+=1
res = dict({})
for k in range(1,n+1):
    if scrs[k]>res.get(k,0):
        res[k] = scrs[k]
    k+=1

max_v = min(res.keys()) 
for key,value in res.items():
    if res[max_v] < res[key]:
        max_v = key 
print(max_v)