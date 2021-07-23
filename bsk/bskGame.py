import random
from PIL import Image as img

class GameAction:


    # 생성자를 사용하여 게임 진행 간 필요한 변수를 생성
    def __init__(self):
        # 진행한 숫자를 출력하기 위한 리스트 변수
        self.list = []
        # 게임 진행 숫자 변수
        self.num = 1



    # print문을 통해 플레이어 에게 메뉴얼을 출력해주는 메소드
    def Manual(self):
        print("게임의 참여자는 차례를 정한뒤 1~3 까지 부를 숫자의 범위를 입력하여 "
              "\n마지막에 숫자 범위가 31을 넘어가는 쪽이 게임에서 진다.")



    # 경로를 통해 승리 이미지를 출력해주는 메소드
    def Image_win(self):
        image_win = img.open("./images/win.png")
        image_win.show()




    # 경로를 통해 패배 이미지를 출력해주는 메소드
    def Image_lose(self):
        image_lose = img.open("./images/lose.png")
        image_lose.show()




    #플레이어 게임진행 메소드
    def Player(self):
        while True:
            print("\n\n---------플레이어 차례!!-----------")
            print("부를 갯수를 입력하세요! ex)1~3")
            self.player = input("입력: ")
            # 1 입력 시
            if self.player == "1":
                self.player = 1
                self.list.append(self.num)#리스트에 생성자 num변수를 추가
                self.num += self.player #생성자 num 변수에 부른 갯수를 더해줌
                print(self.list[-self.player:]) # 리스트 슬라이싱을 활용 뒤에서 부터 플레이어가 부른 수까지 출력
                break
                # 2 입력 시
            elif self.player == "2":
                self.player = 2
                # for 문을 사용하여 플레이어가 입력한 수만큼 반복
                for i in range(self.player):
                    # 반복하는 수만큼 리스트 변수에 넣어줌
                    self.list.append(self.num)
                    # 반복하는 수만큼 +1 씩 num변수를 증가
                    self.num += 1
                # 리스트 슬라이싱을 활용 뒤에서 부터 플레이어가 부른 수까지 출력
                print(self.list[-self.player:])
                break
            elif self.player == "3":
                self.player = 3
                for i in range(self.player): # for 문을 사용하여 플레이어가 입력한 수만큼 반복
                    # 반복하는 수만큼 리스트 변수에 넣어줌
                    self.list.append(self.num)
                    # 반복하는 수만큼 +1 씩 num변수를 증가
                    self.num += 1
                # 리스트 슬라이싱을 활용 뒤에서 부터 플레이어가 부른 수까지 출력
                print(self.list[-self.player:])
                break
            # 1~3 이외에 입력 시 예외 처리
            else:
                print("다시입력하세요!")
                continue
        return self.list, self.num # 진행한 리스트변수 list와 num변수를 메인.py에 반환


    #컴퓨터 쉬움 모드 메소드
    def Computer_easy_mode(self):
        print('\n\n----------컴퓨터 차례!!------------')
        # random 함수를 활용하여 1~3 까지의 난수를 생성
        self.computer = random.randint(1, 3)
        # 생성한 난수를 포문을 통해 난수 만큼 반복
        for a in range(self.computer):
            # 반복하는 수만큼 리스트 변수에 넣어줌
            self.list.append(self.num)
            # 반복하는 수만큼 +1 씩 num변수를 증가
            self.num += 1
        # 리스트 슬라이싱을 활용 뒤에서 부터 난수의 갯수 까지 출력
        print(self.list[-self.computer:])
        # 진행한 리스트변수 list와 num변수를 메인.py에 반환
        return self.list, self.num



    # 컴퓨터 어려움 모드 메소드
    # 베스킨라빈스31 게임은 1대1 일 경우 각자 3개씩만 부를수 있으므로 2,6,10,14,18,22,26,30 순으로 부르면 이기게 됨
    # 즉 컴퓨터는 플레이어가 위 숫자 이외에 숫자를 부를 경우 컴퓨터는 위 숫자를 순서대로 부르게 만든 메소드
    def Computer_hard_mode(self):
        print('\n\n----------컴퓨터 차례!!------------')
        if self.num == 1: # 변수의 담긴 숫자가 1일경우
            for i in range(2): # 반복문을 통해 변수 num의 수가 2가 될때 까지 반복
                self.list.append(self.num) #반복 수만큼 리스트에 추가
                self.num += 1 # 반복 수만큼 변수 num +1 증가
            print(self.list[-2:]) # 리스트 슬라이싱을 활용 뒤에서 부터 플레이어가 부른 수까지 출력
        elif self.num == 2: # 플레이어가 1개 불렀을 경우
            self.list.append(self.num)#리스트에 진행중인 변수 한개만 넣어준뒤
            self.num += 1# 게임 진행 변수를 +1
            print("[", self.list[-1], "]") #숫자 2를 출력하여 필승법 숫자를 부르게 만듬
        elif self.num == 3: # 플레이어가 필승법 숫자를 불렀을 경우
            self.computer = random.randint(1, 3)#1~3 까지 난수를 생성
            for a in range(self.computer): # 난수의 수만큼 반복
                self.list.append(self.num) # 난수의 수만큼 리스트 변수에 추가
                self.num += 1 #난수의 수만큼 num 변수 증가
            print(self.list[-self.computer:]) # 리스트 슬라이싱을 활용 뒤에서 부터 난수의 갯수 까지 출력
        elif self.num == 4: # 이후 플레이어가 필승법 숫자를 부를시엔 난수 아닐시엔 컴퓨터가 2,6,10,14,18,22,26,30 순으로 부르게 설정
            for i in range(3):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-3:])
        elif self.num == 5:
            for i in range(2):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-2:])
        elif self.num == 6:
            self.list.append(self.num)
            self.num += 1
            print("[", self.list[-1], "]")
        elif self.num == 7:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-self.computer:])
        elif self.num == 8:
            for i in range(3):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-3:])
        elif self.num == 9:
            for i in range(2):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-2:])
        elif self.num == 10:
            self.list.append(self.num)
            self.num += 1
            print("[", self.list[-1], "]")
        elif self.num == 11:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-self.computer:])
        elif self.num == 12:
            for i in range(3):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-3:])
        elif self.num == 13:
            for i in range(2):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-2:])
        elif self.num == 14:
            self.list.append(self.num)
            self.num += 1
            print("[", self.list[-1], "]")
        elif self.num == 15:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-self.computer:])
        elif self.num == 16:
            for i in range(3):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-3:])
        elif self.num == 17:
            for i in range(2):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-2:])
        elif self.num == 18:
            self.list.append(self.num)
            self.num += 1
            print("[", self.list[-1], "]")
        elif self.num == 19:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-self.computer:])
        elif self.num == 20:
            for i in range(3):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-3:])
        elif self.num == 21:
            for i in range(2):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-2:])
        elif self.num == 22:
            self.list.append(self.num)
            self.num += 1
            print("[", self.list[-1], "]")
        elif self.num == 23:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-self.computer:])
        elif self.num == 24:
            for i in range(3):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-3:])
        elif self.num == 25:
            for i in range(2):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-2:])
        elif self.num == 26:
            self.list.append(self.num)
            self.num += 1
            print("[", self.list[-1], "]")
        elif self.num == 27:
            self.computer = random.randint(1, 3)
            for a in range(self.computer):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-self.computer:])
        elif self.num == 28:
            for i in range(3):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-3:])
        elif self.num == 29:
            for i in range(2):
                self.list.append(self.num)
                self.num += 1
            print(self.list[-2:])
        elif self.num == 30:
            self.list.append(self.num)
            self.num += 1
            print("[", self.list[-1], "]")
        elif self.num == 31:
            self.list.append(self.num)
            self.num += 1
            print("[", self.list[-1], "]")
        #변환된 리스트 변수 list와 변수 num을 반환
        return self.list, self.num
