def split_and_join(line):
    a = line.split(" ")
    s = ""
    for i in a:
        s = s+"-"+i
    return(s[1:len(s)+1])

    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
