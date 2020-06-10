import pyautogui as pa
import os
import time


ls2 = []
while True:
    count = 0
    ls = []
    choose = int(input("1. 마우스 위치 등록, 2. 마우스 현재 위치 확인, 3. 매크로 시작 4. 등록된 매크로 보기\n>>> "))
    if choose ==  1:
        position_x = int(input("x 좌표 : "))
        position_y = int(input("y 좌표 : "))
        ls.append(position_x)
        ls.append(position_y)
        ls2.append(ls)
        print(ls2)
        time.sleep(1)
        os.system('cls')

    if choose == 2:
        while True:
            my_position = str(pa.position())
            my_position = my_position.replace('Point','')
            my_position = my_position.replace('(','')
            my_position = my_position.replace(')','')
            my_position = my_position.replace('x=','')
            my_position = my_position.replace('y=','')
            print(my_position)
            count += 1
            time.sleep(0.2)
            if  count == 10:
                break
        choosing = int(input("\n\n마지막 좌표를 등록 하시겠습니까? \n\n1. 등록, \n2. 등록 안함\n>>> "))
        if choosing == 1:
            print(my_position,"을 등록했습니다.")
            my_position = my_position.replace(' ','')
            my_position_list = my_position.split(',')
            ls.append(my_position_list[0])
            ls.append(my_position_list[1])
            ls2.append(ls)
            print("\n"+str(ls2))
            time.sleep(1)
            os.system('cls')
        if  choosing == 2:
            print("\n\n")


    if choose == 3:
        num = int(input("몇 번 실행하기겠습니까? 0번은 무한\n>>> "))
        flag = True
        if num == 0:
            while flag:
                for i in range(len(ls2)):
                    pa.moveTo(int(ls2[i][0]),int(ls2[i][1]))
                    time.sleep(0.2)
                    pa.click()
                    time.sleep(0.2)

        else:
            a = 0
            while num > a:
                for i in range(len(ls2)):
                    pa.moveTo(int(ls2[i][0]),int(ls2[i][1]))
                    time.sleep(0.2)
                    pa.click()
                    if keyboard.is_pressed('q'):
                        break
                    time.sleep(0.2)
                    a += 1
                os.system('cls')




    if choose == 4:
        st = str(ls2)
        st = st.replace('[','')
        st = st.replace(']','')
        st_list = st.split(',')
        st = []
        x = []
        y = []
        Ls = []
        for i in range(0,len(ls2) * 2,2):
            x.append(st_list[i])

        for i in range(1,len(ls2) * 2,2):
            y.append(st_list[i])

        for i in range(len(x)):
            st2 = "x 좌표 :"+x[i]+"\ty 좌표 :"+y[i]+"\n"
            Ls.append(st2)

        for i in range(len(Ls)):
            print(Ls[i])
        print("총 갯수 : %d\n\n"%len(Ls))
