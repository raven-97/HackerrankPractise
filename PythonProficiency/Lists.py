if __name__ == '__main__':
    N = int(input())
    m = list()
    for i in range(N):
        c = input()
        cmd = c.split()
        if cmd[0] == "print":
            print(m)
        elif cmd[0] == "sort":
            m.sort()
        elif cmd[0] == "pop":
            m.pop()
        elif cmd[0] == "reverse":
            m.reverse()
        elif cmd[0] == "insert":
            m.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "append":
            m.append(int(cmd[1]))
        elif cmd[0] == "remove":
            m.remove(int(cmd[1]))
        
        
        

