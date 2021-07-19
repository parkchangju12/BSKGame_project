import bskGame
import pyautogui


play = bskGame.Game() # 모듈 불러오기
turn = 0 # 공수
while True:
    choice = input("1:게임규칙 \n2:게임시작\n입력:")
    if choice == "1": # 게임 규칙 선택
        choice=1
        play.Manual()
        choice -= 1
        continue
    elif choice == "2": # 게임 시작
        pyautogui.press(";")
        print("난이도를 선택하세요 \n1:쉬움 2:어려움")
        choice = input("입력: ")
        if choice == "1": # 난이도 쉬움
            while True:
                pyautogui.press(";")
                print("차례를 정하세요. ex)1:선공 2:후공")
                choice1 = input("입력: ")
                if choice1 == "1": # 선공
                    break
                elif choice1 == "2": # 후공
                    turn += 1
                    break
                else:
                    pyautogui.press(";")
                    print("다시입력하세요!")
                    continue
            while True:
                if turn == 0:
                    play.Player()
                    turn += 1
                elif turn == 1:
                    play.Computer_easy_mode()
                    turn -= 1

                if play.num >= 32:
                    break

        elif choice == "2": # 난이도 어려움
            while True:
                pyautogui.press(";")
                print("차례를 정하세요. ex)1:선공 2:후공")
                choice1 = input("입력: ")
                if choice1 == "1":
                    break
                elif choice1 == "2":
                    turn += 1
                    break
                else:
                    pyautogui.press(";")
                    print("다시입력하세요!")
                    continue

            while True:
                if turn == 0:
                    play.Player()
                    turn += 1
                elif turn == 1:
                    play.Computer_hard_mode()
                    turn -= 1
                if play.num >= 32:
                    break

        else:
            print("다시입력하세요!")
    else:
        print("다시입력하세요!")

    if play.num >= 31:
        break

if turn == 0:
    print("플레이어 승리!!")
    play.Image_win()
else:
    print("컴퓨터 승리...")
    play.Image_lose()