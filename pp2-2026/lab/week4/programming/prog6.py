"""
==================================================
 - 작성자: 박지연
 - 작성일: 2026-10-02
 - 문제: 06 Person 클래스
 - 설계:
   1) Person 클래스를 정의한다.
   2) 이름, 휴대폰 번호, 직장 전화번호, 이메일을 저장한다.
   3) 각 정보를 설정하고 반환할 수 있도록 setter/getter 메서드를 작성한다.
   4) __str__() 메서드를 이용하여 Person 객체의 정보를 출력한다.
   5) test_prob6() 함수에서 Person 객체를 생성하고 정보를 출력한다.
==================================================
"""


class Person():
    def __init__(self, n, m="", o="", e=""):
        self.name = n
        self.mobile = m
        self.office = o
        self.email = e

    def __str__(self):
        return "이름: " + self.name + ", 휴대폰 번호: " + self.mobile + ", 직장 전화번호: " + self.office + ", 이메일: " + self.email

    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setMobile(self, m):
        self.mobile = m

    def getMobile(self):
        return self.mobile

    def setOffice(self, o):
        self.office = o

    def getOffice(self):
        return self.office

    def setEmail(self, e):
        self.email = e

    def getEmail(self):
        return self.email


def test_prob6():
    p1 = Person("kim", "", "1234567", "kim@company.com")

    p2 = Person("park", "", "2345678", "")
    p2.setEmail("park@company.com")

    print(p1)
    print(p2)


if __name__ == "__main__":
    test_prob6()
