#회원가입 프로그램

print('=========================')
print("회원가입")
print('=========================')

register = False

while not register:
    print("회원가입을 진행하시겠습니다?\n Y:진행   N:취소")
    register_input = input('>>  ')
    register_input = register_input.lower()

    if register_input == 'y':
        register = True
        print('회원가입이 진행이 됩니다')

    elif register_input == 'n':
        print("회원가입이 취소됩니다")
        exit()
    else:
        print("올바른 값을 입력해주세요")


users = [] #리스트생성

while True:

    user = {} #딕셔너리생성

    username = input('ID: ')
    while True:
        password = input('PW: ')
        password_confirm = input('PW 확인: ')
        if password == password_confirm:
            break
        else:
            print('패스워드가 일치하지 않습니다')
    name = input('이름: ')
    while True:
        birth_date = input('생년월일(6자리): ')
        if len(birth_date) == 6:
            break
        else:
            print('생년월일을 다시 입력해주세요(6자리)')
    email = input('이메일: ')

    user['username'] = username
    user['password'] = password
    user['name'] = name
    user['birth_date'] = birth_date
    user['email'] = email
    

    users.appent(user) #users 리스트에 user의 정보를 저장하는 과정
    print(users)


    print("==========================")
    print(f"{user['name']}님 가입을 환영합니다!")
    print("==========================")

    print('회원가입을 추가로 진행하시겠습니까?\n y:진행      N:c취소')

    register_another_input = input('>> ')
    register_another_input = register_another_input.lower()

    if register_another_input =='y':
        pass
    elif register_another_input == 'n':
        exit()

        











           

