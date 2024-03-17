import random
import inputimeout

def input_in_3sec():
    try:
        return inputimeout.inputimeout(timeout=3)
    except inputimeout.TimeoutOccurred:
        return None

def win():
    print("게임에 승리하셨습니다!")

def defeat():
    print("게임에 패배하셨습니다.")

class RSP_Game:
    def __init__(self):
        self.RSP = ['가위', '바위', '보']
        self.user_RSP = None

    def choose_RSP(self):
        while True:
          
            print("가위/바위/보를 입력하세요. :", end = " ")
            self.user_RSP = input()
            
            if self.user_RSP in self.RSP:
                break
            else:
                print("다시 입력해주세요.")

    def play_RSP(self):
        computer_RSP = random.choice(self.RSP)
        print("상대는 " + computer_RSP + "을 냈습니다.")
        print("3초 안에 이겼다/졌다/개굴을 입력하세요. :", end = " ")
        user_answer = input_in_3sec()

        if user_answer == None:
            defeat()

        elif self.user_RSP == computer_RSP:
            if user_answer == '개굴':
                win()
            else:
                defeat()

        elif self.user_RSP == '가위' and computer_RSP == '보' or \
        self.user_RSP == '바위' and computer_RSP == '가위' or \
        self.user_RSP == '보' and computer_RSP == '바위':
            if user_answer == '이겼다':
                win()
            else:
                defeat()

        else:
            if user_answer == '졌다':
                win()
            else:
                defeat()
            

def game_play():
    game = RSP_Game()
    game.choose_RSP()
    game.play_RSP()

if __name__ == '__main__':

    while True:
        
        print("게임을 시작하시겠습니까?(Y/N) :", end = " ")
        isGameStart = input()

        if isGameStart.upper() == 'Y':
            print("게임을 시작합니다.")
            game_play()
        elif isGameStart.upper() == 'N':
            print("게임을 종료합니다.")
            break
        else:
            print("'Y'나 'N'을 입력해주세요.")