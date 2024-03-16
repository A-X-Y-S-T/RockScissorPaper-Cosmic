import os

while True:
    print("게임을 시작하시겠습니까?(Y/N)", end=" ")
    isGameStart = input()

    if isGameStart == 'Y' or 'y':
        print("게임을 시작합니다.")
        break
    elif isGameStart == 'N' or 'n':
        print("게임을 종료합니다.")
        break
    else:
        print("'Y'나 'N'으로 입력해주세요.")

print("end")