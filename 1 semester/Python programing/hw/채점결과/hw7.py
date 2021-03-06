
'''
Coding Style
   - redundancy :
   - minor error :
   - major error : -3
Poor Documentation :
Logical Error :
Compilation Error :
Score : 97/100
TA's comment : The game is not ended after satisfying ending condition.
'''

# Assignment Number... : 7
# Student Name........ : 이현호
# File Name........... : hw7_이현호
# Program Description. : 제어문을 제어문을 활용하여 재미있는 프로그램을 만들어보는 과제입니다.

print('''  [전략게임 : 포켓몬스터 진화시키기]

             게임 규칙 :
                 (1) 키우고 싶은 포켓몬을 3마리 중에 한마리를 선택한다.
             
                 (2) 공복도가 100이 되거나, 스테미너가 0이 되면 포켓몬은 도망칩니다.
                         
                 (3) 체력과 힘이 100이 되면 진화를 할 수 있습니다.
                         
                 (4) 진화조건이 충족되면 진화를 할 수 있습니다.(무조건 진화를 해야합니다.)
                     
                 (5) 진화가 완료되면 게임은 종료됩니다.
''')

print('당신이 키울수 있는 포켓몬은 피카츄, 파이리, 꼬부기입니다.')                                           # print()함수를 사용하여 키울수 있는 포켓몬을 보여줍니다.

while True:                                                                                                  # while문을 사용하여 무한루프를 만듭니다.(1번 루프문)
    while True:                                                                                              # while문을 사용하여 무한루프를 만듭니다.(2번 루프문)
        mon = input('당신이 키우고 싶은 포켓몬을 입력하세요...: ')                                           # input함수를 통해 포켓몬을 입력 받습니다.
        if mon == '피카츄' or mon == '파이리' or mon == '꼬부기':                                            # 포켓몬의 이름에 따라 기본상태스텟을 다르게 부여합니다.
            print('\n{}를 성공적으로 진화시키면 게임이 종료됩니다.\n'.format(mon))
            if mon == '피카츄':
                mon_p = 15
                mon_s = 10
                mon_f = 0
                mon_e = 100
                print('기본스탯\n체력......: {}\n힘........: {}\n공복도....: {}\n스테미너..: {}\n'.
                      format(mon_p, mon_s,mon_f, mon_e))
                break
            elif mon == '꼬부기':
                mon_p = 10
                mon_s = 15
                mon_f = 0
                mon_e = 100
                print('기본스탯\n체력......: {}\n힘........: {}\n공복도....: {}\n스테미너..: {}\n'.
                      format(mon_p, mon_s,mon_f, mon_e))
                break
            else:
                mon_p = 12
                mon_s = 13
                mon_f = 0
                mon_e = 100
                print('기본스탯\n체력......: {}\n힘........: {}\n공복도....: {}\n스테미너..: {}\n'.
                      format(mon_p, mon_s,mon_f, mon_e))
                break                                                                                         # 각 if문에서 포켓몬에 따른 스탯을 부여한 후 무한루프문을 정지합니다.(2번 루프문 종료)

    i = 1                                                                                                     # 몇번 째 날인지 알기 위해 i = 1를 할당하고,
    while True:                                                                                               # while문과 print함수를 통해 무한 루프로 출력합니다.(3번 루프문)
        print('\n{}번째 날\n'.format(i))

        while True:                                                                                           # while무한루프문을 통해 각 날에 시행할 활동을 부여합니다.(4번 루프문)
            print('무엇을 하시겠습니까?\
                \n1. 체력훈련, 2. 힘훈련, 3. 밥먹기, 4. 휴식하기\
                \n\n체력훈련을 할 경우 체력이 증가합니다.\
                \n힘훈련을 할 경우 힘이 증가합니다.\
                \n밥먹기를 할 경우 공복도수치가 감소합니다.\
                \n휴식하기를 할 경우 스테미너가 증가합니다.\n')                                               # print함수를 통해 각 활동에 대한 설명을 합니다.
            action = input()                                                                                  # input함수를 통해 활동을 입력을 받습니다.
            if action == '1' or action == '2' or action == '3' or action == '4' or\
            action == '체력훈련' or action == '힘훈련' or action == '밥먹기' or action == '휴식하기':
                break                                                                                         # 올바르게 활동에 대한 입력을 했을 시 무한루프를 정지합니다.(4번 루프문 종료)
            else:
                print('입력이 잘못되었습니다.')                                                               # if문을 통해 잘못된 입력을 했을시 다시 입력을 받습니다.(4번 루프문 처음으로 돌아감.)

        if action == '1' or action == '체력훈련':                                                             # 각 활동에 대한 입력이 1 혹은 체력훈련 인 경우를 if문을 사용하여 스탯을 재할당합니다.
            mon_p += 10
            mon_f += 15
            mon_e -= 20
            if mon_f >= 100:
                mon_f = 0
                if mon_e <= 0:
                    mon_e = 0
                    print('{}가 가혹한 스케쥴을 인해 도망갔습니다...\
                    \n원인 : 스테미너 수치 0이하로 떨어짐.'.format(mon))
                    break                                                                                      # 스테미너 수치가 0이하로 떨어지는 경우 3번 루프문을 종료합니다.(3번 루프문 종료)
                else:
                    print('{}가 배고파서 도망갔습니다...\
                    \n원인 : 공복도 100이상으로 올라감.'.format(mon))
                    break                                                                                      # 공복도가 100이상으로 올라가는 경우 3번 루프문을 종료합니다.(3번 루프문 종료)
            else:
                if mon_e <= 0:
                    mon_e = 0
                    print('{}가 가혹한 스케쥴을 인해 도망갔습니다...\
                    \n원인 : 스테미너 수치 0이하로 떨어짐.'.format(mon))
                    break                                                                                      # 스테미너 수치가 0이하로 떨어지는 경우 3번 루프문을 종료합니다.(3번 루프문 종료)
            print('체력훈련을 선택하셨습니다.\n\n체력스탯이 증가합니다.\
                  \n공복도가 증가합니다.\n스테미너가 감소합니다.')
            print('\n기본스탯\n체력......: {}\n힘........: {}\n공복도....: {}\n스테미너..: {}\n'.
                  format(mon_p, mon_s,mon_f, mon_e))                                                           # print함수를 통해 재할당된 스탯을 사용자에게 출력하여 보여줍니다.

        elif action == '2' or action == '힘훈련':                                                              # 각 활동에 대한 입력이 2 혹은 힘훈련 인 경우를 if문을 사용하여 스탯을 재할당합니다.
            mon_s += 10
            mon_f += 20
            mon_e -= 15
            if mon_f >= 100:
                mon_f = 100
                if mon_e <= 0:
                    mon_e = 0
                    print('{}가 가혹한 스케쥴을 인해 도망갔습니다...\
                    \n원인 : 스테미너 수치 0이하로 떨어짐.'.format(mon))       
                    break                                                                                      # 스테미너 수치가 0이하로 떨어지는 경우 3번 루프문을 종료합니다.(3번 루프문 종료)
                else:
                    print('{}가 배고파서 도망갔습니다...\
                    \n원인 : 공복도 100이상으로 올라감.'.format(mon))
                    break                                                                                      # 공복도가 100이상으로 올라가는 경우 3번 루프문을 종료합니다.(3번 루프문 종료)
            else:
                if mon_e <= 0:
                    mon_e = 0
                    print('{}가 가혹한 스케쥴을 인해 도망갔습니다...\
                    \n원인 : 스테미너 수치 0이하로 떨어짐.'.format(mon))
                    break                                                                                      # 스테미너 수치가 0이하로 떨어지는 경우 3번 루프문을 종료합니다.(3번 루프문 종료)
            print('힘훈련을 선택하셨습니다.\n\n힘스탯이 증가합니다.\
                  \n공복도가 증가합니다.\n스테미너가 감소합니다.')
            print('\n기본스탯\n체력......: {}\n힘........: {}\n공복도....: {}\n스테미너..: {}\n'.
                  format(mon_p, mon_s,mon_f, mon_e))                                                           # print함수를 통해 재할당된 스탯을 사용자에게 출력하여 보여줍니다.

        elif action == '3' or action == '밥먹기':                                                              # 각 활동에 대한 입력이 3 혹은 밥먹기 인 경우를 if문을 사용하여 스탯을 재할당합니다.
            mon_f -= 30
            mon_e += 10
            if mon_f <= 0:
                mon_f = 0
                if mon_e >= 100:
                    mon_e = 100
            else:
                if mon_e >= 100:
                    mon_e = 100
                elif mon_e <= 0:
                    mon_e = 0
            print('밥먹기를 선택하셨습니다.\n\n공복도가 감소합니다.\
                  \n스테미너가 증가합니다.')
            print('\n기본스탯\n체력......: {}\n힘........: {}\n공복도....: {}\n스테미너..: {}\n'.
                  format(mon_p, mon_s,mon_f, mon_e))                                                            # print함수를 통해 재할당된 스탯을 사용자에게 출력하여 보여줍니다.

        elif action == '4' or action == '휴식하기':                                                             # 각 활동에 대한 입력이 4 혹은 휴식하기 인 경우를 if문을 사용하여 스탯을 재할당합니다.
            mon_e += 50
            if mon_e >= 100:
                mon_e = 100
            print('휴식하기를 선택하셨습니다.\n\n스테미너가 증가합니다.')
            print('\n기본스탯\n체력......: {}\n힘........: {}\n공복도....: {}\n스테미너..: {}\n'.
                  format(mon_p, mon_s,mon_f, mon_e))                                                            # print함수를 통해 재할당된 스탯을 사용자에게 출력하여 보여줍니다.

        if mon_p >= 100 and mon_s >= 100:                                                                       # if문을 사용하여 체력, 힘 스탯이 100이상이 됐을 때,
            while True:                                                                                         # while문을 사용하여 무한루프를 합니다.(5번 루프문)
                print('축하드립니다.\n진화를 할 수 있습니다\n진화를 하시겠습니까?\
                \n원하면 y 원하지 않으면 n을 누르세요.')                                                        # print함수를 통해 진화가 가능함을 사용자에게 보여줍니다.
                yes_no = input()                                                                                # 진화를 하기위해 사용자에게 y를 입력받습니다.
                if yes_no == 'y':                                                                               # 사용자가 y를 입력한 경우 각각의 포켓몬의 명칭을 재할당합니다.
                    print('진화를 시작합니다')
                    if mon == '피카츄':
                        mon = '라이츄'
                    elif mon == '파이리':
                        mon = '망나뇽'
                    else:
                        mon = '어니부기'
                    break                                                                                       # 정상적으로 재할당되면 무한루프문을 종료합니다.(5번 루프문 종료)
                else:
                    while True:                                                                                 # y를 누르지않았을 때를 대비한 무한루프문을 while문을 통해 실행합니다.(6번 루프문)
                        yes_no = input('y를 누르세요...: ')
                        if yes_no == 'y':                                                                       # y를 눌렀다면 정상적으로 새로운 포켓몬 명칭을 재할당 받습니다.
                            print('진화를 시작합니다.')
                            if mon == '피카츄':
                                mon = '라이츄'
                            elif mon == '파이리':
                                mon = '망나뇽'
                            else:
                                mon = '어니부기'
                            break                                                                               # 정상적으로 재할당하면 루프문을 종료합니다.(5번 루프문 종료)
                    break                                                                                       # 정상적으로 진화를 했을 때, 루프문을 종료합니다.(6번 루프문 종료)                                                                                      
            
            break                                                                                               # 정상적으로 마무리 되면 루프문을 종료합니다.(3번 루프문 종료)
        
        i += 1
    if mon == '망나뇽' or mon == '어니부기' or mon == '라이츄':                                                 # 만약 포켓몬의 이름이 바뀐다면,
        print('진화에 성공하였습니다. {}가 되었습니다. 축하합니다.'.format(mon))                                # 진화가 성공했음을 사용자에게 보여줍니다.
        break                                                                                                   # break를 사용해 최종루프문을 종료합니다.(1번 루프문 종료)
