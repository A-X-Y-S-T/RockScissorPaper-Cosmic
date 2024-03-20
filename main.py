import random
import inputimeout

score = 0
combo_count = 1

def win():
    print("게임에 승리하셨습니다!")
    global score
    global combo_count
    score = score + combo_count

def defeat():
    print("게임에 패배하셨습니다.")
    global score
    global combo_count
    score = 0
    combo_count = 1

def combo():
    global combo_count
    combo_count = combo_count + 1
    print("Combo! +", combo_count)

def input_in_3sec():
    """3초 동안만 입력을 받는 함수"""

    try:
        return inputimeout.inputimeout(timeout=3)
    except inputimeout.TimeoutOccurred:
        return None
    
class RSP_Game:
    def __init__(self):
        self.RSP = ['가위', '바위', '보']
        self.user_pick = None

    #가위바위보 선택 함수
    def choose_RSP(self):
        while True:
          
            print("가위/바위/보를 입력하세요. :", end = " ")
            self.user_pick = input()
            
            if self.user_pick in self.RSP:
                break
            else:
                print("다시 입력해주세요.")

    #가위바위보 실행 함수
    def play_RSP(self):

        computer_pick = random.choice(self.RSP)
        print("상대는 " + computer_pick + "을 냈습니다.")
        print("3초 안에 이겼다/졌다/개굴을 입력하세요. :", end = " ")
        user_answer = input_in_3sec()

        if user_answer == None:
            print("Time Over!")
            defeat()

        elif self.user_pick == computer_pick:
            if user_answer == '개굴':
                win()
            else:
                defeat()

        elif self.user_pick == '가위' and computer_pick == '보' or \
        self.user_pick == '바위' and computer_pick == '가위' or \
        self.user_pick == '보' and computer_pick == '바위':
            if user_answer == '졌다':
                combo()
                win()
            else:
                defeat()

        else:
            if user_answer == '이겼다':
                global combo_count
                combo_count = 1
                win()
            else:
                defeat()

#게임 반복 실행
while True:

    print("게임을 하시겠습니까?(Y/N) :", end = " ")
    isGameStart = input()

    if isGameStart.upper() == 'Y':
        print("게임을 시작합니다.")
        print("현재 점수는 " + str(score) + "점입니다.")

        game = RSP_Game()
        game.choose_RSP()
        game.play_RSP()

    elif isGameStart.upper() == 'N':
        print("게임을 종료합니다.")
        break
    else:
        print("'Y'나 'N'을 입력해주세요.")