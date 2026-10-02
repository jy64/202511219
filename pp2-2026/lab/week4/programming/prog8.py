"""
==================================================
 - 작성자: 박지연
 - 작성일: 2026-10-02
 - 문제: 08 클래스와 객체를 이용한 노래 출력
 - 설계:
   1) PrintSong 클래스를 정의한다.
   2) 생성자(__init__)에서 노래 가사를 리스트로 전달받는다.
   3) sing() 메서드를 이용하여 가사를 한 줄씩 출력한다.
   4) test_prob8() 함수에서 PrintSong 객체를 생성하고 sing()을 호출한다.
==================================================
"""


class PrintSong():
    def __init__(self, strings):
        self.strings = strings

    def sing(self):
        for line in self.strings:
            print(line)


def test_prob8():
    aSong = PrintSong([
        "TWINKLE, twinkle, Little star",
        "How I wonber what you are!",
        "Up above the world so high,",
        "Like a diamond in the sky."
    ])

    aSong.sing()


if __name__ == "__main__":
    test_prob8()
