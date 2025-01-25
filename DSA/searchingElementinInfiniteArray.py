# this code will only work for searching an element which actually exists in the array
# In order to make it work for all the cases, we need to add the return statements where we don't find the target

arr = [2,3,4,6,9,12,15,19,23,26,28,30,35,38]
target = 25



def findRange(arr, target):
    start = 0
    end = 1
    while target>arr[end]: # this while loop only checks the condition. it doesn't matter if the target is actually present in the array or not. 
        newStart = end+1
        end = end + (end-start+1)*2
        start = newStart    #changing the start value after using it in the pervious line.
    return [start,end]


# this will print the elements separately which are returned as an array from findRange().
print(findRange(arr,target)[0])
print(findRange(arr,target)[1])

def binarySearch(arr,target):
    start = findRange(arr,target)[0]
    end = findRange(arr,target)[1]
    while start <=end:
        mid = (start+end)//2
        if target == arr[mid]:
            return mid
        elif target>arr[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1

print(f"Index of the target is: {binarySearch(arr,target)}")