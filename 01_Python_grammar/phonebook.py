contact = {}

def phone_number(number):
    return number.isdigit() or ('-' in number)

while True:
    print('-----전화번호부 프로그램-----')
    print('1.추가   2.보기   3.검색   4.수정   5.삭제   9.종료')
    try:
        menu = int(input('메뉴를 선택해주세요.(숫자만): ' ))
    except ValueError:
        print('잘못된 입력입니다. 숫자를 입력해주세요:)')
        continue

    if menu == 1:
        print('연락처를 추가합니다.')
        
        new_name = input('이름: ')
        if not new_name:
            print('이름이 비어있습니다. 다시 입력해주세요:)')
            continue
            
        new_tel = input('전화번호: ')
        if not phone_number(new_tel):
            print('전화번호 형식이 잘못되었습니다. 다시 입력해주세요:)')
            continue
        print(new_name, new_tel)
        # contact[new_name] = new_tel
        contact.setdefault(new_name, new_tel)

    elif menu == 2: #완성
        print('연락처를 조회합니다.')
        # print(contact)
        if not contact:
            print('해당 연락처가 없습니다.')
        else:
            for name, tel in contact.items():
                print(name, '=', tel )

    elif menu == 3: # 완성
        print('연락처를 검색합니다.')
        search_name = input('검색 이름: ')
        # print(contact[search_name])
        if not search_name:
            print('검색할 이름을 입력해주세요.')
            continue
        print(contact.get(search_name, '없는 이름입니다.'))


    elif menu == 4: # 완성
        print('연락처를 수정합니다.')
        mod_name = input('수정 이름 : ')
        if not mod_name:
            print('수정할 이름을 입력해주세요.')
            continue

        if mod_name in contact:
            mod_tel = input('새 전화번호 : ')
            if not phone_number(mod_tel):
                print('전화번호 형식이 잘못되었습니다. 다시 입력해주세요:)')
                continue
            contact[mod_name] = mod_tel
        else :
            print('등록되지 않은 이름입니다.')

    elif menu == 5: # 완성
        print('연락처를 삭제합니다.')
        del_name = input('삭제 이름: ')
        if not del_name:
            print('삭제할 이름을 입력해주세요.')
            continue

        if del_name in contact:
            del contact[del_name]
        else :
            print('등록되지 않은 이름입니다.')


    elif menu == 9: # 완성
        print('연락처를 종료합니다.')
        break

    else :
        print('잘못된 입력입니다.')