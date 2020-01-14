# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
mydict = defaultdict(list)
for i in range(n):
    s = input()
    mydict[s].append(i+1)
#print(mydict)
for i in range(m):
    k = input()
    print(*mydict.setdefault(k, [-1]),sep = ' ')


