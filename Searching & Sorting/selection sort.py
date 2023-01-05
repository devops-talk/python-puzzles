

from sys import stdin

def selectionSort(array, size):
    for step in range(size):
        minimum_idx = step
        for i in range(step + 1, size):
            if array[i] < array[minimum_idx]:
                minimum_idx = i


def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    selectionSort(arr, n)
    printList(arr, n)

    t-= 1