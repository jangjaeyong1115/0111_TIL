import sys
sys.stdin = open("input7.txt","r")
test_case,number = map(int,input().split())
print(test_case,number)
for i in range(test_case):
    for j in range(number):
        numbers = list(map(int,input().split()))
        for n in numbers:
            print(n,end=" ")
        print()