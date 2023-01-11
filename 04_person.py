# 소개팅
# 사람 관련 정보

class Person:

    def __init__(self,name,age,mbti,location):
        self.name = name
        self.age = age
        self.mbti = mbti
        self.location = location

    def greeting(self):
        return f'{self.name}입니다. {self.mbti}이구요...'

    def __gt__(self, other):
        if self.age > other.age:
            return self
        else:
            return other

    def __str__(self):
        return f'{self.name}({self.age})'
            

p1 = Person('재용', 28, 'esfj','서울')
p2 = Person('유영', 30, 'infp','경기')

print(p1.name)
print(p2.name)
print(p1.location)
print(p2.location)
print(p1.greeting())
print(p2.greeting())
print(p1 > p2)
print(p1 < p2)
