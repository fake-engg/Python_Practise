# Binary search on a list (sorted in ascending order)

'''

list = [-31,-22,-10,0,2,6,20,31,45,69,71,101,150]
target = int(input('Enter the target: '))

def binarySearch(list, target):
    start = 0
    end = len(list)-1
    while start <= end:
        mid = (start + end)//2
        if target > list[mid]:
            start = mid + 1
        elif target < list[mid]:
            end = mid - 1
        else:
            return mid
    return -1

print(binarySearch(list,target))

'''

# Order-agnostic binary search (sorted data structure but unknown of the behavious of the sorting)

# list = [-31,-22,-10,0,2,6,20,31,45,69,71,101,150]

list = [150,120,98,80,77,53,41,29,15,9,0,-23,-51,-97]
target = int(input('Enter the target: '))

def orderAgnostic(list,target):
    start = 0
    end = len(list)-1
    isAsc = True if list[start]<list[end] else False

    while start <= end:
        mid = (start+end)//2
        if list[mid] == target:
            return mid
        if isAsc == True:
            if target < list[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > list[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

print(orderAgnostic(list,target))