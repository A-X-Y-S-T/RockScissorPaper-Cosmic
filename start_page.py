import multiprocessing as mp

def Game():
    print("가위바위보")


if __name__ == '__main__':
    while True:
        print("게임을 시작하시겠습니까?(Y/N)", end = " ")
        isGameStart = input()

        if isGameStart == 'Y' or isGameStart == 'y':
            print("게임을 시작합니다.")
            pid = mp.Process(target=Game)
            pid.start(); pid.join()
        elif isGameStart == 'N' or isGameStart == 'n':
            print("게임을 종료합니다.")
            break
        else:
            print("'Y'나 'N'을 입력해주세요.")