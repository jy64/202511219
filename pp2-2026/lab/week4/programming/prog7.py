"""
==================================================
 - 작성자: 박지연
 - 작성일: 2026-10-02
 - 문제: 07 전화번호부 클래스
 - 설계:
   1) phoneBook 클래스를 정의한다.
   2) contacts 딕셔너리를 이용하여 이름과 전화번호, 이메일을 저장한다.
   3) add() 메서드를 이용하여 연락처를 추가한다.
   4) __str__() 메서드를 이용하여 전화번호부 내용을 출력한다.
   5) test_prob7() 함수에서 전화번호부 객체를 생성하고 연락처를 추가한다.
==================================================
"""


class phoneBook():
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, email=None):
        self.contacts[name] = {
            "office": office,
            "email": email
        }

    def __str__(self):
        result = ""

        for name in self.contacts:
            result = result + name + "\n"
            result = result + "office phone: " + self.contacts[name]["office"] + "\n"
            result = result + "email address: " + self.contacts[name]["email"] + "\n\n"

        return result


def test_prob7():
    obj = phoneBook()

    obj.add("kim", office="1234567", email="kim@company.com")
    obj.add("park", office="2345678", email="park@company.com")

    print(obj)


if __name__ == "__main__":
    test_prob7()
