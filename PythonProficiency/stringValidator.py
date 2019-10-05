import re
if __name__ == '__main__':
    s = input()
print(bool(re.search('[0-9a-zA-Z]+', s)))
print(bool(re.search('[a-zA-Z]+',s)))
print(bool(re.search('[0-9]+',s)))
print(bool(re.search('[a-z]+',s)))
print(bool(re.search('[A-Z]+',s)))





