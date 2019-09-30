if __name__ == '__main__':
    mark = list()
    student = list()
    for _ in range(int(input())):
        name = input()
        student.append(name)
        score = float(input())
        mark.append(score)
    for i in range(len(mark)-1):
        for j in range(len(mark)-1):
            if mark[j] > mark[j+1]:
                mark[j+1], mark[j] = mark[j], mark[j+1]
                student[j+1], student[j] = student[j], student[j+1]
    f = 0
    for l in range(len(mark)):
        if mark[l]> min(mark):
            f = l
            break
    m = list()

    for k in range(f, f+mark.count(mark[f])):
        m.append(student[k])
    m.sort()
    for e in m:
        print(e)



