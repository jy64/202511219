"""
==================================================
 - 작성자: 박지연
 - 작성일: 2026-10-02
 - 문제: 02 Rocket 클래스
 - 설계:
   1) Rocket 클래스를 정의한다.
   2) 로켓의 x, y 위치를 저장한다.
   3) moveUp() 메서드를 이용하여 로켓의 높이를 1씩 증가시킨다.
   4) test_prob2() 함수에서 Rocket 객체를 생성한다.
   5) 로켓의 현재 높이를 출력하고 moveUp()을 실행한 후
      변경된 높이를 출력한다.
==================================================
"""


class Rocket():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "로켓의 위치: (" + str(self.x) + ", " + str(self.y) + ")"

    def moveUp(self):
        self.y = self.y + 1


def test_prob2():
    myRocket = Rocket()

    print("로켓의 높이:", myRocket.y)

    myRocket.moveUp()

    print("로켓의 높이:", myRocket.y)


if __name__ == "__main__":
    test_prob2()
