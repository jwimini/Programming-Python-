from Luck import Luck
from Constellation import Constellation

def go():
    print("1.운세보기")
    print("2.별자리 운세")
    print("3.종료하기")
    number = input("보고싶은 운세를 선택하세요: ")
    return number

def main():
    luck = Luck()
    star = Constellation()
    # go()
    while True:
        number=go()
        if number=='1':
            luck.show_menu()
        elif number=='2':
            star.show_menu()
        elif number == '3':
            break
        else:
            print("다시입력하세요")

if __name__ == '__main__':
    main()