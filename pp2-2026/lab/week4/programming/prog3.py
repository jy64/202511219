"""
==================================================
 - 작성자: 박지연
 - 작성일: 2026-10-02
 - 문제: 03 Box 클래스
 - 설계:
   1) Box 클래스를 정의한다.
   2) 상자의 길이, 높이, 깊이를 저장한다.
   3) 각 크기를 설정하고 반환할 수 있도록 setter/getter 메서드를 작성한다.
   4) test_prob3() 함수에서 Box 객체를 생성한다.
   5) 상자의 길이, 높이, 깊이를 이용하여 부피를 계산하고 출력한다.
==================================================
"""


class Box():
    def __init__(self, length=100, height=100, depth=100):
        self.l = length
        self.h = height
        self.d = depth

    def __str__(self):
        return "(" + str(self.l) + ", " + str(self.h) + ", " + str(self.d) + ")"

    def setlength(self, length):
        self.l = length

    def getLength(self):
        return self.l

    def setHeight(self, height):
        self.h = height

    def getHeight(self):
        return self.h

    def setDepth(self, depth):
        self.d = depth

    def getDepth(self):
        return self.d


def test_prob3():
    b1 = Box(100, 100, 100)

    print(b1)
    print("상자의 부피는:", b1.getHeight() * b1.getLength() * b1.getDepth())


if __name__ == "__main__":
    test_prob3()
