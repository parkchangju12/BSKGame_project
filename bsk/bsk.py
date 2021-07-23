import bskGame
import pyautogui


play = bskGame.GameAction() # 모듈 불러오기
turn = 0 # 차례 관련 변수 (0: 플레이어 차례 1: 컴퓨터 차례)
while True:
    MenuChoice = input("1:게임규칙 \n2:게임시작\n입력:") # 게임 규칙 및 게임시작 선택
    # MenuChoice 문자형 1일시 (문자형으로 받는 이유: 숫자형 1로 받을 시 문자형으로 플레이어가 입력하면 오류 발생 원인)
    if MenuChoice == "1":
        MenuChoice = 1 # 문자형으로 받은 변수를 숫자형으로 변환
        play.Manual() # 게임 설명 메뉴얼 메소드
        continue # 메뉴얼 글을 띄어준 후 이전 MenuChoice 변수 선택
    elif MenuChoice == "2": # 게임 시작
        # 창 초기화 (파이썬 내 내장함수인 pyautogui의 메소드인 press를 사용하여 자동으로 콘솔 창을 초기화해줌)
        pyautogui.press(";")
        print("난이도를 선택하세요 \n1:쉬움 2:어려움")
        LevelChoice = input("입력: ") # 난이도 선택
        if LevelChoice == "1": # 난이도 쉬움
            while True:
                pyautogui.press(";")
                print("차례를 정하세요. ex)1:선공 2:후공")
                TurnChoice = input("입력: ") #공수 선택
                if TurnChoice == "1": # 선공
                    break
                elif TurnChoice == "2": # 후공
                    turn += 1
                    break
                # 공수선택 부분 예외처리
                else:
                    pyautogui.press(";")
                    print("다시입력하세요!")
                    continue
            while True:#게임 진행(난이도{하})
                if turn == 0:
                    play.Player()
                    turn += 1
                elif turn == 1:
                    play.Computer_easy_mode()
                    turn -= 1
                if play.num >= 32:
                    break




        elif LevelChoice == "2": # 난이도 어려움
            while True:
                pyautogui.press(";")
                print("차례를 정하세요. ex)1:선공 2:후공")
                TurnChoice = input("입력: ") #공수 선택
                if TurnChoice == "1": #선공
                    break
                elif TurnChoice == "2": #후공
                    turn += 1
                    break
                else:# 공수선택 부분 예외처리
                    pyautogui.press(";")
                    print("다시입력하세요!")
                    continue
            while True:#게임 진행(난이도{상})
                if turn == 0:
                    play.Player()
                    turn += 1
                elif turn == 1:
                    play.Computer_hard_mode()
                    turn -= 1
                if play.num >= 32:
                    break
        else:#난이도 선택 부분 예외 처리
            print("다시입력하세요!")
    # 게임 규칙 및 게임 시작 선택 부분 예외 처리
    else:
        print("다시입력하세요!")
    # 함수의 변수 가 31을 넘었을 경우 반복문 종료
    if play.num >= 31:
        break
# 플레이어 차례일때 반복문이 종료 됬을시
if turn == 0:
    print("플레이어 승리!!")
    # 승리관련 이미지 불러오기
    play.Image_win()
# 컴퓨터 차례일때 반복문이 종료 됬을시
else:
    print("컴퓨터 승리...")
    # 패배 관련 이미지 불러오기
    play.Image_lose()