"""
==================================================
 - 작성자: 박지연
 - 작성일: 2026-10-02
 - 문제: 05 Triangle 클래스
 - 설계:
   1) Triangle 클래스를 정의한다.
   2) 삼각형의 세 각과 변의 수를 저장한다.
   3) getAngles()를 이용하여 삼각형의 각도를 반환한다.
   4) setAngles()를 이용하여 삼각형의 각도를 변경한다.
   5) checkAngles()를 이용하여 세 각의 합이 180도인지 확인한다.
   6) test_prob5() 함수에서 Triangle 객체를 생성하고 결과를 출력한다.
==================================================
"""


class Triangle():
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.numberOfSides = 3

    def __str__(self):
        return "변의 수: " + str(self.numberOfSides) + ", 각도: " + str(self.getAngles())

    def setAngles(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def getAngles(self):
        return (self.a1, self.a2, self.a3)

    def checkAngles(self):
        if self.a1 + self.a2 + self.a3 == 180:
            return True
        else:
            return False


def test_prob5():
    triangle = Triangle(90, 30, 60)

    print(triangle)
    print(triangle.checkAngles())


if __name__ == "__main__":
    test_prob5()
