import sys
sys.stdin = open("input5.txt","r")
test_case = int(input())
print(test_case)
for i in range(test_case):
    number = int(input())
    print(number)
    for j in range(number):
        a = list(input().split("\n"))
        for n in a:
            print(n)