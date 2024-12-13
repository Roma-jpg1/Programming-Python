import PySimpleGUI as sg
import random
import os
sg.theme("DarkGray14")
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()
ttem=["Манчестер Сити","Реал Мадрид",
     "Арсенал","Интер Милан",
     "Байер Леверкузен", "Ливерпуль",
     "Барселона", "Бавария Мюнхен"]
ish=[]
layout = [
    [sg.Text('', size=(11, 1)), sg.Text("Футбольчик", font=("Arial", 35, 'bold'), justification="center")],
    [sg.Text('', size=(15, 1)), sg.Button('Добавить команду', font=('Arial', 14), size=(20,1)), sg.Text('', size=(15, 1))],
    [sg.Text('', size=(15, 1)), sg.Button('Удалить команду', font=('Arial', 14), size=(20,1)), sg.Text('', size=(15, 1))],
    [sg.Text('', size=(15, 1)), sg.Button('Экспорт файла', font=('Arial', 14), size=(20,1)), sg.Text('', size=(15, 1))],
    [sg.Text('', size=(15, 1)), sg.Button('Импорт файла', font=('Arial', 14), size=(20,1)), sg.Text('', size=(15, 1))],
    [sg.Text('', size=(15, 1)), sg.Button('Создать турнир', font=('Arial', 14), size=(20,1)), sg.Text('', size=(15, 1))],
    [sg.Text('', size=(15, 1)), sg.Button('Эмуляция турнира', font=('Arial', 14), size=(20,1)), sg.Text('', size=(15, 1))]
]
window=sg.Window("", layout)
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    elif event == 'Добавить команду':
        layout1 = [
            [sg.Text("Введите название команды", font=("Arial", 24, 'bold'), justification="center", pad=(0, 20))],
            [sg.Text("Добавление команды:", font=("Arial", 14)),
             sg.InputText(key='addteam', font=("Arial", 14), size=(20, 1), pad=(0, 10))],
            [sg.Button('OK', font=('Arial', 16), button_color=('white', 'blue'), pad=(0, 20))],
        ]
        window1=sg.Window("", layout1)
        while True:
            event1, values1 = window1.read()
            if event1 == sg.WINDOW_CLOSED:
                break
            if event1 == 'OK':
                print(values1['addteam'])
                if values1['addteam']=='':
                    layoutI0 = [
                        [sg.Image(filename=r"C:\Users\Roman P\Desktop\im11.png")],
                        [sg.Text('', size=(17, 1)),sg.Text('!Введите название команды!', font=('Arial', 20), text_color='white')],
                        [sg.Button('Закрыть')]
                    ]
                    windowI0 = sg.Window('Ошибка', layoutI0)
                    while True:
                        eventI0, valuesI0 = windowI0.read()
                        if eventI0 == sg.WIN_CLOSED or eventI0 == 'Закрыть':
                            break

                    windowI0.close()
                else:
                    k=0
                    for i in ttem:
                        if i == values1['addteam']:
                            sg.popup_error("такая команда уже есть введите другую")
                            k+=1
                    if k == 0:
                        ttem.append(values1['addteam'])
                        break
        window1.close()
    elif event == 'Удалить команду':
        layout2 = [
            [sg.Text("Введите название команды", font=("Arial", 24), justification="center", size=(30, 1),
                     pad=(10, 10))],
            [sg.Text("Удаление команды:", font=("Arial", 16), size=(15, 1)),
             sg.InputText(key='rmteam', font=('Arial', 16), size=(20, 1))],
            [sg.Button('OK', font=('Arial', 16), button_color=('white', 'blue'), pad=(0, 20))]
        ]
        window2 = sg.Window("", layout2)
        while True:
            event2, values2 = window2.read()
            if event2 == sg.WINDOW_CLOSED:
                break
            if event2 == 'OK':
                if values2['rmteam'] =='':
                    # ///////////////////////////////
                    layoutI = [
                        [sg.Image(filename=r"C:\Users\Roman P\Desktop\im11.png")],
                        [sg.Text('', size=(17, 1)),sg.Text('!Введите название команды!', font=('Arial', 20), text_color='white')],
                        [sg.Button('Закрыть')]
                    ]
                    windowI = sg.Window('Ошибка', layoutI)
                    while True:
                        eventI, valuesI = windowI.read()
                        if eventI == sg.WIN_CLOSED or eventI == 'Закрыть':
                            break

                    windowI.close()
                    # ---------------------
                else:
                    k = 0
                    for j in ttem:
                        if j == values2['rmteam']:
                            k += 1
                            ttem.remove(values2['rmteam'])
                            print(ttem)
                    if k == 0:
                        sg.popup_error("такой команды нет введите другую")
                    else:
                        break
        window2.close()
    elif event == 'Экспорт файла':
        file_path = sg.popup_get_file('Выберите файл для экспорта', save_as=True, no_window=True, file_types=(('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')))
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                for item in ttem:
                    file.write(item + '\n')
            sg.popup('Экспорт завершен успешно.')


    elif event == 'Импорт файла':
        layout3 = [
            [sg.Text('Выберите файл для импорта данных:')],
            [sg.Input(key="path"), sg.FileBrowse()],
            [sg.Button('Импортировать'), sg.Button('Выход')],
            [sg.Listbox(values=[], size=(40, 10), key='LIST')]
        ]
        window3 = sg.Window('', layout3)
        while True:
            event3, values3 = window3.read()
            if event3 == sg.WINDOW_CLOSED or event3 == 'Выход':
                break

            if event3 == 'Импортировать':
                file_path = values3["path"]
                file_data = read_file(file_path)
                window3['LIST'].update(values=file_data)
                ttem=[]
                for m in file_data:
                    if m[-1]=="\n":
                        ttem.append(m[:-1])
                    else:
                        ttem.append(m)

        window3.close()

    elif event == 'Создать турнир':
        layout4 = [
            [sg.Text("Введите название турнира:", font=('Arial', 14)), sg.InputText(key='nametur', font=('Arial', 14))],
            [sg.Text("Введите количество команд:", font=('Arial', 14)), sg.InputText(key='ctur', font=('Arial', 14))],
            [sg.Button('ОК', font=('Arial', 16), button_color=('white', '#4CAF50')),
             sg.Button('Отмена', font=('Arial', 16), button_color=('white', '#F44336'))]
        ]
        window4 = sg.Window('', layout4)
        while True:
            event4, values4 = window4.read()
            if event4 == sg.WINDOW_CLOSED or event4 == 'Отмена':
                break
            if event4 == 'ОК':
                if values4['ctur']:
                    if int(values4['ctur'])%2!=0 or int(values4['ctur'])>len(ttem) or int(values4['ctur'])==0:
                        sg.popup("невозможное количество команд в турнире")
                    else:
                        pr=ttem
                        sport=[]
                        ish=[]
                        for l in range(int(values4['ctur'])):
                            random_item = random.choice(pr)
                            pr.remove(random_item)
                            ish.append(random_item)
                        directory = 'rgr_f'
                        for s in range(0,len(ish)-1,2):
                            sport.append(f"{ish[s]} - {ish[s+1]}")
                        if not os.path.exists(directory):
                            os.makedirs(directory)
                        file_path = os.path.join(directory, f'{values4["nametur"]}.txt')
                        with open(file_path, 'w') as file:
                            file.write(f'{values4["nametur"]}\n')
                            file.write('\n')
                            for p in range(0,len(ish)-1,2):
                                file.write(f"{ish[p]} - {ish[p+1]}\n")

                        print(f'Список успешно записан в файл {file_path}')
                        break
                else:
                    layoutI01 = [
                        [sg.Image(filename=r"C:\Users\Roman P\Desktop\im33.png")],
                        [sg.Text('!Введите название команды!', font=('Arial', 20), text_color='white')],
                        [sg.Button('Закрыть')]
                    ]
                    windowI01 = sg.Window('Ошибка', layoutI01)
                    while True:
                        eventI01, valuesI01 = windowI01.read()
                        if eventI01 == sg.WIN_CLOSED or eventI01 == 'Закрыть':
                            break

                    windowI01.close()
    elif event =='Эмуляция турнира':
        if len(ish)>0:

            win=[]
            ran=[]
            for q in range(0,len(sport)*2,2):
                g1=random.randint(0,10)
                g2=random.randint(0,10)
                ran.append(str(g1)+':'+str(g2))
                if g1>g2:
                    win.append(ish[q])
                elif g1<g2:
                    win.append(ish[q+1])
                else:
                    win.append(ish[q + 1]+' = '+ish[q])
            j=0
            for j in range(len(sport)):
                sport[j]= (sport[j] + ' ' + str(ran[j]))

            with open(file_path, 'w') as file:
                file.write(f'{values4["nametur"]}\n')
                file.write('\n')
                p=0
                for p in range(len(sport)):
                    file.write(f'{sport[p]} \n')
                file.write('\n')
                file.write('\n')
                p=0
                for p in range(len(win)):
                    file.write(f'{win[p]} \n')
            layoutI1 = [
                [sg.Image(filename=r"C:\Users\Roman P\Downloads\im22.png")],
                [sg.Text('', size=(17, 1)),
                 sg.Text('Команды успешно сыграли!', font=('Arial', 20), text_color='white')],
                [sg.Button('УРА')]
            ]
            windowI1 = sg.Window('', layoutI1)
            while True:
                eventI1, valuesI1 = windowI1.read()
                if eventI1 == sg.WIN_CLOSED or eventI1 == 'УРА':
                    break
            windowI1.close()
        else:
            layout5 = [
                [sg.Text("Введите название турнира:", font=('Arial', 14)),
                 sg.InputText(key='nametur1', font=('Arial', 14))],
                [sg.Text("Введите количество команд:", font=('Arial', 14)),
                 sg.InputText(key='ctur1', font=('Arial', 14))],
                [sg.Button('ОК', font=('Arial', 16), button_color=('white', '#4CAF50')),
                 sg.Button('Отмена', font=('Arial', 16), button_color=('white', '#F44336'))]
            ]
            window5 = sg.Window('', layout5)
            while True:

                event5, values5 = window5.read()
                if event5 == sg.WINDOW_CLOSED:
                    window5.close()
                    break

                if event5=='Отмена':
                    window5.close()
                    break
                if event5 == 'ОК':
                    if values5['ctur1']:

                        pr = ttem
                        sport = []
                        ish = []
                        if int(values5['ctur1']) % 2 != 0 or int(values5['ctur1']) > len(ttem) or int(values5['ctur1'])==0:
                            sg.popup("невозможное количество команд в турнире")
                        else:
                            for l in range(int(values5['ctur1'])):
                                random_item = random.choice(pr)
                                pr.remove(random_item)
                                ish.append(random_item)
                            directory = 'rgr_f'
                            for s in range(0, len(ish) - 1, 2):
                                sport.append(f"{ish[s]} - {ish[s + 1]}")
                            if not os.path.exists(directory):
                                os.makedirs(directory)
                            file_path = os.path.join(directory, f'{values5["nametur1"]}.txt')
                            with open(file_path, 'w') as file:
                                file.write(f'{values5["nametur1"]}\n')
                                file.write('\n')
                                for p in range(0, len(ish) - 1, 2):
                                    file.write(f"{ish[p]} - {ish[p + 1]}\n")

                            print(f'Команды успешно записаны в файлиk {file_path}')
                            layoutI1 = [
                                [sg.Image(filename=r"C:\Users\Roman P\Downloads\im22.png")],
                                [sg.Text('', size=(17, 1)),
                                 sg.Text('Команды успешно сыграли!', font=('Arial', 20), text_color='white')],
                                [sg.Button('УРА')]
                            ]
                            windowI1 = sg.Window('', layoutI1)
                            while True:
                                eventI1, valuesI1 = windowI1.read()
                                if eventI1 == sg.WIN_CLOSED or eventI1 == 'УРА':
                                    break

                            windowI1.close()
                            # ---------------
                            win = []
                            ran = []
                            for q in range(0, len(sport) * 2, 2):
                                g1 = random.randint(0, 10)
                                g2 = random.randint(0, 10)
                                ran.append(str(g1) + ':' + str(g2))
                                if g1 > g2:
                                    win.append(ish[q])
                                elif g1 < g2:
                                    win.append(ish[q + 1])
                                else:
                                    win.append(ish[q + 1] + ' = ' + ish[q])
                            j = 0
                            for j in range(len(sport)):
                                sport[j] = (sport[j] + ' ' + str(ran[j]))

                            with open(file_path, 'w') as file:
                                file.write(f'{values5["nametur1"]}\n')
                                file.write('\n')
                                p = 0
                                for p in range(len(sport)):
                                    file.write(f'{sport[p]} \n')
                                file.write('\n')
                                file.write('\n')
                                p = 0
                                for p in range(len(win)):
                                    file.write(f'{win[p]} \n')
# ------------------------------------------

                            print(f'Команды успешно сыграли {file_path}')
                            window5.close()
                    else:
                        window5.close()


window.close()
print(ttem)