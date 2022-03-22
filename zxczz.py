	
import sys
basket = []
while True:
    print("=" * 20)
    print("장바구니입니다.")
    print("=" * 20)
    print(" 1. 담겨있는 물건 확인하기")
    print("\n 2. 물건 추가하기")
    print("\n 3. 물건 삭제하기")
    print("\n 0. 프로그램 종료")
    print("=" * 20)
    select = int(input("무엇을 하실 건가요? (숫자 입력) : "))
 
    while True:
        if select == 1:
            if basket == []:
                print("아무것도 없습니다.")
                break
            else:
                print(basket)
                break
 
        elif select == 2:
            print("추가할 항목을 입력해주세요. 더 이상 추가할 항목이 없으면 '그만'을 입력해주세요.")
            add = input()
            if add == "그만":
                print("장바구니 담기를 종료합니다.")
                break
            else:
                basket.append(add)
 
        elif select == 3:
            if basket == []:
                print("장바구니가 비었습니다. 추가해주세요.")
                break
            else:
                print(basket)
                print("\n\n현재 담겨있는 장바구니 목록입니다. 삭제하실 항목을 입력해주세요.")
                print("삭제 메뉴를 종료하시려면 0을 입력해주세요.")
                delete = input()
 
                if delete in basket:
                    basket.remove(delete)
                    print("삭제가 완료되었습니다.")
 
                elif delete == "0":
                    break
 
                else:
                    print("잘못된 값을 입력하셨습니다. 다시 입력해주세요.")
        elif select == 0:
            print("프로그램을 종료합니다.")
            sys.exit()
 
        else:
            print("잘못 입력했습니다. 다시 입력해주세요.")
            break
