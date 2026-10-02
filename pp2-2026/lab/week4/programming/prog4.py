"""
==================================================
 - 작성자: 박지연
 - 작성일: 2026-10-02
 - 문제: 04 Rectangle 클래스
 - 설계:
   1) Rectangle 클래스를 정의한다.
   2) 사각형의 x, y 좌표와 너비, 높이를 저장한다.
   3) setx()와 getx()를 이용하여 x 좌표를 설정하고 가져온다.
   4) getArea()를 이용하여 사각형의 넓이를 계산한다.
   5) overlap()을 이용하여 두 사각형이 겹치는지 확인한다.
   6) test_prob4() 함수에서 두 개의 Rectangle 객체를 생성하고
      두 사각형의 겹침 여부를 출력한다.
==================================================
"""


class Rectangle():
    def __init__(self, x=0, y=0, w=100, h=100):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return "사각형: (" + str(self.x) + ", " + str(self.y) + ", " + str(self.width) + ", " + str(self.height) + ")"

    def setx(self, x):
        self.x = x

    def getx(self):
        return self.x

    def getArea(self):
        return self.width * self.height

    def overlap(self, r):
        if self.x + self.width <= r.x:
            return False
        if r.x + r.width <= self.x:
            return False
        if self.y + self.height <= r.y:
            return False
        if r.y + r.height <= self.y:
            return False
        return True


def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)

    if r1.overlap(r2):
        print("r1과 r2는 서로 겹칩니다.")
    else:
        print("r1과 r2는 서로 겹치지 않습니다.")


if __name__ == "__main__":
    test_prob4()
