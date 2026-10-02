"""
==================================================
 - 작성자: 박지연
 - 작성일: 2026-10-02
 - 문제: 01 Cat 클래스
 - 설계:
   1) Cat 클래스를 정의한다.
   2) 고양이의 이름과 나이를 저장한다.
   3) setName()과 getName()을 이용하여 이름을 설정하고 가져온다.
   4) __str__() 메서드를 이용하여 고양이의 이름과 나이를 출력한다.
   5) test_prob1() 함수에서 두 개의 Cat 객체를 생성하고 출력한다.
==================================================
"""


class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "," + str(self.age)

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


def test_prob1():
    missy = Cat('Missy', 3)
    lucky = Cat('Lucky', 5)

    print(missy)
    print(lucky)


if __name__ == "__main__":
    test_prob1()
