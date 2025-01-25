#Search for an element in a list
'''
lis = eval(input('Enter the list: '))
target = int(input('Enter the target no: '))

def searchValue(lis,target):
    if len(lis) == 0:
        return "Empty list"
    for x in range(len(lis)):
        if lis[x] == target:
            return x
        else:
            return 'Target not found..'
    
        
print(searchValue(lis,target))

'''

#Search for a character in a string


'''
str = input("Enter the string: ")
char = input("Enter the character: ")

def searchChar(str, char):
    if len(str) ==0:
        return 'Empty string'
    for x in str:
        if x == char:
            return True
        else: 
            False

print(searchChar(str, char))

'''

# Find the min value in the list

'''

list = eval(input('Enter the list: '))

def findMin(list):
    min = list[0]
    for x in range(1,len(list)):
        if min > list[x]:
            min = list[x]

    return min

print(f"Smallest element in the list is: {findMin(list)}")

'''

# Searching in 2D list

'''

mat = [
    [2,6,9],
    [32,73,6,9],
    [12,29,76,41],
    [62,5,87]
]

target = 76

def search2D(mat,target):
    for row in range(len(mat)):
        # print('Row:',row)
        # print('Len of mat: ',len(mat))
        for col in range(len(mat[row])):
            # print('Col:',col)
            # print('Len of 1st element',len(mat[row]))
            if target == mat[row][col]:
                return row,col
    return -1
            
indices = search2D(mat,target)
print(f"Target {target} is present at indices: {indices}")

'''

# Find the no of even digit elements in a list

'''


nums = eval(input("Enter the list: "))


def findNumbers(nums):
    noOfElements = 0
    for x in nums:
        print(x)
        count=0        
        while x>0:
            count+=1
            x = x//10
        if count % 2 == 0:
            noOfElements +=1
    return noOfElements

print(findNumbers(nums))

'''
#Efficient approach of previous question

'''


import math
nums = eval(input("Enter the list: "))


def findNumbers(nums):
    noOfElements = 0
    for x in nums:
        count = 0
        count = int(math.log10(x)+1)
        if count%2 ==0:
            noOfElements +=1
    return noOfElements

print(findNumbers(nums))

'''

#Leetcode: 1672 - Richest customer wealth


class Solution:
    def maximumWealth(self, accounts) -> int:
        wealth = 0
        for x in accounts:
            sum = 0
            # wealth = 0
            for y in x:
                sum = sum+y
            if sum>wealth:
                wealth = sum
        return wealth

        