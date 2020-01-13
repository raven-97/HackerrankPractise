# Enter your code here. Read input from STDIN. Print output to STDOUT
stamp = dict()
n = input()
for i in range(int(n)):
    s = input()
    stamp[s] = stamp.get(s,0)+1
print(len(stamp.keys()))
