# https://leetcode.com/problems/peak-index-in-a-mountain-array/


# Brute force solution - O(N) time-complexity
'''
arr = [0,1,0]

prev = arr[0]
for i in range(len(arr)): # check each element with the previous element, once the element starts decreasing record the position and the element
    if arr[i] >= prev:
        prev = arr[i]
    else:
        prev = arr[i-1]
        index = i-1
        break

print(f" Peak element is: {prev} and it is present at: {index}")

'''

# Optimized solution - O(logN) complexity

arr = [1,4,6,7,4,2]
def findPeak(arr):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid]<arr[mid+1]:
            start = mid+1
        elif arr[mid]<arr[mid-1]:
            end = mid-1
        else:
            return mid
    return arr[start]

print(findPeak(arr))

'''
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid-1]>arr[mid]:
            end = mid-1
        elif arr[mid]>arr[mid+1]:
            start = mid+1
    return arr[start]
'''


# Peak of mountain array which ahs multiple peaks. However, we can return any one of the peak

#https://leetcode.com/problems/find-peak-element/
#Leetcode:162

class Solution:
    def findPeakElement(self, nums):
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start+end)//2
            #this logic compares the two elements to understand the sorting behaviour
            # first logic is to pass the test case when there is only 1 element present in the array
            if mid < len(nums)-1 and nums[mid]<nums[mid+1]:
                start = mid+1
            elif nums[mid]<nums[mid-1]:
                end = mid-1
            else:
                return mid
        return nums[start]