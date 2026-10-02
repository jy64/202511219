"""
==================================================
 - 작성자: 홍길동
 - 작성일: 2026-10-03
 - 문제: 09 터틀 그래픽 객체 이동
 - 설계:
   1) turtle 모듈을 이용하여 화면을 생성한다.
   2) Turtle()을 이용하여 원 모양과 거북이 모양의 객체를 각각 생성한다.
   3) 첫 번째 터틀은 왼쪽 방향으로 계단식 경로를 이동시킨다.
   4) 두 번째 터틀은 오른쪽 방향으로 계단식 경로를 이동시킨다.
   5) 각 터틀의 이동 경로가 화면에 나타나도록 한다.
==================================================
"""

import turtle


def test_prob9():
    # 화면 설정
    win = turtle.Screen()

    # 1. 첫 번째 거북이 (t1) - 검은 원 모양
    t1 = turtle.Turtle()
    t1.shape("circle")
    t1.color("black")

    # 2. 두 번째 거북이 (t2) - 거북이 모양
    t2 = turtle.Turtle()
    t2.shape("turtle")
    t2.color("black")

    # t1(원) 이동 경로 작성
    t1.left(180)
    t1.forward(150)
    t1.right(90)
    t1.forward(20)
    t1.left(90)
    t1.forward(150)

    # t2(거북이) 이동 경로 작성
    t2.forward(150)
    t2.right(90)
    t2.forward(20)
    t2.left(90)
    t2.forward(150)

    # 창이 바로 닫히지 않도록 대기
    turtle.done()


if __name__ == "__main__":
    test_prob9()
