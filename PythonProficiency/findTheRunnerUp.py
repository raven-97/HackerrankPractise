if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
a = list(arr)
a.sort(reverse = True)
print(a[a.count(a[0])])

