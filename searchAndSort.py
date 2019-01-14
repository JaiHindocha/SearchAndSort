import random
import time

def bubbleSortAsc(arr):
    for i in range(0,len(arr)-1):
        for j in range (0,len(arr)-1):
            if (arr[j])>(arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def bubbleSortDesc(arr):
    for i in range(0,len(arr)-1):
        for j in range (0,len(arr)-1):
            if (arr[j])<(arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


def mergeSortAsc(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        right = arr[mid:]
        left = arr[:mid]

        mergeSortAsc(left)
        mergeSortAsc(right)

        x=y=z=0

        while y < len(right) and x < len(left):
            if left[x] <= right[y]:
                arr[z] = left[x]
                x = x + 1
            else:
                arr[z] = right[y]
                y = y + 1
            z = z + 1

        while x < len(left):
            arr[z]=left[x]
            x=x+1
            z=z+1

        while y < len(right):
            arr[z]=right[y]
            y=y+1
            z=z+1

    return arr

def mergeSortDesc(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        right = arr[mid:]
        left = arr[:mid]

        mergeSortDesc(left)
        mergeSortDesc(right)

        x=y=z=0

        while y < len(right) and x < len(left):
            if left[x] >= right[y]:
                arr[z] = left[x]
                x = x + 1
            else:
                arr[z] = right[y]
                y = y + 1
            z = z + 1

        while x < len(left):
            arr[z]=left[x]
            x=x+1
            z=z+1

        while y < len(right):
            arr[z]=right[y]
            y=y+1
            z=z+1

    return arr


def linearSearch(arr,searchNum):
    for i in range(0, len(arr)-1):
        if arr[i] == searchNum:
            return True
    return False

def binarySearch(arr,searchNum):
    sortedArr = mergeSortAsc(arr)
    first=0
    last=len(sortedArr)-1
    while last >= first:
        mid = (first+last)//2
        if sortedArr[mid]==searchNum:
            return True
        elif sortedArr[mid] < searchNum:
            first = mid + 1
        elif sortedArr[mid] > searchNum:
            last = mid - 1

    return False

def binarySearchSorted(sortedArr,searchNum):
    first=0
    last=len(sortedArr)-1
    while last >= first:
        mid = (first+last)//2
        if sortedArr[mid]==searchNum:
            return True
        elif sortedArr[mid] < searchNum:
            first = mid + 1
        elif sortedArr[mid] > searchNum:
            last = mid - 1

    return False

class Node:
    def __init__(self,value):
        self.value = int(value)
        self.leftNode= None
        self.rightNode = None

    def insert(self,newValue):
        if newValue < self.value:
            if self.leftNode != None:
                self.leftNode.insert(newValue)
            else:
                self.leftNode = Node(newValue)

        elif newValue > self.value:
            if self.rightNode != None:
                self.rightNode.insert(newValue)
            else:
                self.rightNode = Node(newValue)

    def search(self,searchNum):
        if searchNum < self.value:
            if self.leftNode is None:
                return False
            return self.leftNode.search(searchNum)
        elif searchNum > self.value:
            if self.rightNode is None:
                return False
            return self.rightNode.search(searchNum)
        elif searchNum == self.value:
            return True

def binarySearchTree(arr,searchNum):
    tree = Node(arr[0])
    for i in range(1,len(arr)):
        tree.insert(int(arr[i]))
    itemFound = tree.search(searchNum)
    return itemFound
