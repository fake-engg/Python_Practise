#https://leetcode.com/problems/find-in-mountain-array/
#function to find the peak of the array



nums = [1,2,4,6,8,10,4,2,1]
target = 1

# this function find the peak element of the array and return its index
def findPeakElement(nums):
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)//2
            #this logic compares the two elements to understand the sorting behavious
            # first logic is to pass the test case when there is only 1 element present in the array
            if mid < len(nums)-1 and nums[mid]<nums[mid+1]:
                start = mid+1
            elif nums[mid]<nums[mid-1]:
                end = mid-1
            else:
                return mid    # this will return the peak element
        return start

# this function does the binary search. 
#once we get the peak element's index, we can say that from start to peak, the array would be in ascending.
# and after index (peak+1) till end, it will be descending

# so we are deviding the array using the peak and then doing the binary search in the 2 sections to find the target element
def orderAgnostic(nums,target,start, end):
    # start = 0
    # end = len(list)-1
    isAsc = True if nums[start]<nums[end] else False

    while start <= end:
        mid = (start+end)//2
        if nums[mid] == target:
            return mid
        if isAsc == True:
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

# this function is the main driving function that gives the index value of the target element
def findValue(nums,target):
    peak = findPeakElement(nums)    # we are taking the peak element using the function
    firstValue = orderAgnostic(nums,target,0,peak) # based on the peak element, we will be doing the binary search in the first section of the array (0-peak).
    if firstValue != -1: # if firstValue() ==-1, it means we did not get the target in the ascending section of the array. so it will check the descending section(else part).
        return firstValue
    else:
        return orderAgnostic(nums,target,peak+1,len(nums)-1) # Since we have searched from 0 to peak in the firt part, now we will search the target from peak+1 till the end of the array.
    
    

print(findValue(nums, target))
