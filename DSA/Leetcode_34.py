nums = [5,7,7,8,8,10]
target =6
def defineRange(nums,target):
    start = 0
    end = len(nums)-1
    Range = []
    while start<=end:
        mid=(start+end)//2
        if target == nums[mid]:
            fwd,rnd = mid,mid
            while fwd<len(nums) and nums[fwd] == target:
                fwd+=1
            while rnd>=0 and nums[rnd]==target:
                rnd-=1
            Range.append(rnd+1)
            Range.append(fwd-1)
            return Range
            # for i in range(mid+1):
            #     if nums[i]==target:
            #         # print(nums[i])
            #         Range.append(i)
            #         break
            #     else:
            #         continue
            # # Range.append(mid)
            # for j in range(mid+1, len(nums)):
            #     if nums[j]==target:
            #         while nums[j]==target:
            #             j+=1
            #         Range.append(j-1)
            #         break
            #     else:
            #         Range.append(mid)
            # return Range
        if target>nums[mid]:
            start = mid+1
            # print(start)
            # print(mid)
        else:
            end = mid-1
            # print("mid value: ",mid)
        
            
    return [-1,-1]
    
print(defineRange(nums,target))