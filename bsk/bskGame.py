import random
from PIL import Image as img

class Game:
    def __init__(self):
        self.list_2 = []
        self.num = 1


    def Manual(self):
        print("게임의 참여자는 차례를 정한뒤 1~3 까지 부를 숫자의 범위를 입력하여 "
              "\n마지막에 숫자 범위가 31을 넘어가는 쪽이 게임에서 진다.")

    def Image_win(self):
        image_win = img.open("./images/win.png")
        image_win.show()

    def Image_lose(self):
        image_lose = img.open("./images/lose.png")
        image_lose.show()

    def Player(self):
        while True:
            print("\n\n---------플레이어 차례!!-----------")
            print("부를 갯수를 입력하세요! ex)1~3")
            self.player = input("입력: ")
            if self.player == "1":
                self.player = 1
                self.list_2.append(self.num)
                self.num += self.player
                print(self.list_2[-self.player:])
                break
            elif self.player == "2":
                self.player = 2
                for i in range(self.player):
                    self.list_2.append(self.num)
                    self.num += 1
                print(self.list_2[-self.player:])
                break
            elif self.player == "3":
                self.player = 3
                for i in range(self.player):
                    self.list_2.append(self.num)
                    self.num += 1
                print(self.list_2[-self.player:])
                break
            else:
                print("다시입력하세요!")
                continue
        return self.list_2, self.num

    def Computer_easy_mode(self):
        print('\n\n----------컴퓨터 차례!!------------')
        self.computer = random.randint(1, 3)
        for a in range(self.computer):
            self.list_2.append(self.num)
            self.num += 1
        print(self.list_2[-self.computer:])

        return self.list_2, self.num

    def Computer_hard_mode(self):
        print('\n\n----------컴퓨터 차례!!------------')
        if self.num == 1:
            for i in range(2):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-2:])
        elif self.num == 2:
            self.list_2.append(self.num)
            self.num += 1
            print("[", self.list_2[-1], "]")
        elif self.num == 3:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-self.computer:])
        elif self.num == 4:
            for i in range(3):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-3:])
        elif self.num == 5:
            for i in range(2):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-2:])
        elif self.num == 6:
            self.list_2.append(self.num)
            self.num += 1
            print("[", self.list_2[-1], "]")
        elif self.num == 7:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-self.computer:])
        elif self.num == 8:
            for i in range(3):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-3:])
        elif self.num == 9:
            for i in range(2):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-2:])
        elif self.num == 10:
            self.list_2.append(self.num)
            self.num += 1
            print("[", self.list_2[-1], "]")
        elif self.num == 11:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-self.computer:])
        elif self.num == 12:
            for i in range(3):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-3:])
        elif self.num == 13:
            for i in range(2):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-2:])
        elif self.num == 14:
            self.list_2.append(self.num)
            self.num += 1
            print("[", self.list_2[-1], "]")
        elif self.num == 15:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-self.computer:])
        elif self.num == 16:
            for i in range(3):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-3:])
        elif self.num == 17:
            for i in range(2):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-2:])
        elif self.num == 18:
            self.list_2.append(self.num)
            self.num += 1
            print("[", self.list_2[-1], "]")
        elif self.num == 19:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-self.computer:])
        elif self.num == 20:
            for i in range(3):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-3:])
        elif self.num == 21:
            for i in range(2):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-2:])
        elif self.num == 22:
            self.list_2.append(self.num)
            self.num += 1
            print("[", self.list_2[-1], "]")
        elif self.num == 23:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-self.computer:])
        elif self.num == 24:
            for i in range(3):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-3:])
        elif self.num == 25:
            for i in range(2):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-2:])
        elif self.num == 26:
            self.list_2.append(self.num)
            self.num += 1
            print("[", self.list_2[-1], "]")
        elif self.num == 27:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-self.computer:])
        elif self.num == 28:
            for i in range(3):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-3:])
        elif self.num == 29:
            for i in range(2):
                self.list_2.append(self.num)
                self.num += 1
            print(self.list_2[-2:])
        elif self.num == 30:
            self.list_2.append(self.num)
            self.num += 1
            print("[", self.list_2[-1], "]")
        elif self.num == 31:
            self.list_2.append(self.num)
            self.num += 1
            print("[", self.list_2[-1], "]")

        return self.list_2, self.num
