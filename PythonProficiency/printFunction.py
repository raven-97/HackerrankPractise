if __name__ == '__main__':
    n = int(input())
s = 0
f = 10
for i in range(1,n+1):
    if i >9:
        f = 100
    if i>99:
        f = 1000

    s =s*f+i
print(s)a

