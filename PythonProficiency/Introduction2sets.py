def average(array):
    # your code goes here
    thisset = set()
    for element in arr:
        thisset.add(element)
    return sum(list(thisset))/len(list(thisset))
    


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
