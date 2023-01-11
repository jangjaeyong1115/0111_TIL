class Person:

    def greeting(self):

        return 'hi...'

IU = Person()
jimin = Person()

print(type(IU))
print(type(jimin))
print(type([1,2,3]))
print(type([]))

# 메서드를 호출할 수 있음
print(IU.greeting())

# 속성을 부여할 수 있음
IU.name = '아이유'
jimin.name = '지민'
print(IU.name)
print(jimin.name)
print(type(IU.name))

'apple banana'.split()[0].upper().strip()[2]
['apple','banana'][0].upper().strip()[2]
'apple'.upper().strip()[2]
'APPLE'.strip()[2]
'APPLE'[2]