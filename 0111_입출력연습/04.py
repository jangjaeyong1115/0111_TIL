import sys
sys.stdin = open("input4.txt","r")
test_case = int(input())
print(test_case)
for i in range(test_case):
    number = int(input())
    print(number)
    for j in range(number):
        numbers = list(map(int,input().split()))
        for n in numbers:
            print(n,end=" ")
        print()