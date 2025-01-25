nums = [4,5,6,7,0,1,2]
# target = 7

def findPeak(nums):
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = (start+end)//2
        fwd, bkd = mid,mid
        while fwd<len(nums) and nums[mid]<nums[mid+1]:
            fwd+=1
        peak = fwd 
        while bkd>0 and nums[mid]>nums[mid-1]:
            bkd-=1
        peak = bkd 
    return peak 

print(findPeak(nums))
