# Ceiling of a number

'''arr = eval(input('Enter an array: '))
target = int(input('Enter the target: '))

def ceiling(arr,target):
        start = 0
        end = len(arr)-1
        while start<=end:
            mid = (start+end)//2
            if target>arr[mid]:
                start = mid+1
            elif target<arr[mid]:
                end = mid-1
            else:
                return mid
        return arr[start]

print(ceiling(arr,target))'''


#Floor of a number in a list

arr = eval(input('Enter an array: '))
target = int(input('Enter the target: '))

def ceiling(arr,target):
        start = 0
        end = len(arr)-1
        while start<=end:
            mid = (start+end)//2
            if target>arr[mid]:
                start = mid+1
            elif target<arr[mid]:
                end = mid-1
            else:
                return mid
        return arr[end]

print(ceiling(arr,target))