if __name__ == '__main__':
    n = int(input())
    student_marks = dict()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = student_marks.get(name,0)+sum(scores)/3
    query_name = input()
    print(format(student_marks[query_name],'.2f'))

