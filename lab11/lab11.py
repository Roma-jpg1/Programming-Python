# задание 1
# dict = {'1':'.,!?:','2': "ABC", '3': "DEF", '4': "GHI",
#                     '5': "JKL",'6': "MNO", '7': "PQRS", '8': "TUV", '9': "WXYZ", '0': ' '}
# a = input().upper()
# k=0
# for i in range(len(a)):
#     for j in range(len(dict)):
#         if a[i] in dict[str(j)]:
#             print(str(j)*(dict[str(j)].index(a[i])+1), end=' ')
# #

# # задание 2
# dict = {'1': "AEILNORSTU", '2': 'DG', '3': 'BCMP', '4': 'FHVWY', '5': 'K', '8': 'JX', '10': 'QZ'}
# a = input().upper()
# c=0
# for i in range(len(a)):
#     for j in dict:
#         if a[i] in dict[str(j)]:
#             c += int(j)
# print(c)

# задание 3
# emails = {'gryffindor.com': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'k_stepanov'],
# 'hufflepuff.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
# 'hogwarts.com': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
# 'slytherin.com': ['ekaterina_ivanova', 'glebova_nastya'],
# 'ravenclaw.com': ['john.doe', 'mark.zuckerberg', 'helen_hunt']}
# for i in emails:
#     for j in emails[i]:
#         print(f"{j}@{i}")


# #задание 4
# import PySimpleGUI as sg
# from random import *
# sg.theme("DarkTeal")
# layout = [
#     [sg.Text('Генератор случайных чисел', font=('Arial', 16), justification='center')],
#     [sg.Text('Введите нижнюю границу:'), sg.InputText(key='l')],
#     [sg.Text('Введите верхнюю границу:'), sg.InputText(key='u')],
#     [sg.Text('Сгенерированное число:', size=(21, 1)), sg.InputText(key='r')],
#     [sg.Button('Сгенерировать', font=('Arial', 14)), sg.Button('Выход', font=('Arial', 14))],
#     [sg.Image(filename="m_cubbbbbbbbb.png")]]
# window = sg.Window("Калькулятор рейтинга по физике", layout)
# while True:
#     event, values = window.read()
#     if event in (sg.WINDOW_CLOSED, "Выход"):
#         break
#     if event == "Сгенерировать":
#         if int(values['l'])>=int(values['u']):
#             sg.popup_error("нижняя граница должна быть ниже верхней")
#         else:
#             random_number = randint(int(values['l']), int(values['u']))
#             window["r"].update(random_number)
# window.close()

# # задание 5
# import PySimpleGUI as sg
# sg.theme("DarkTeal")
# dict = {'1': "AEILNORSTU", '2': 'DG', '3': 'BCMP', '4': 'FHVWY', '5': 'K', '8': 'JX', '10': 'QZ'}
# layout = [
#     [sg.Text('Эрудит', font=('Arial', 19), justification='center')],
#     [sg.Text('Введите слово:'), sg.InputText(key='word')],
#     [sg.Text('Стоимость слова:', size=(15, 1)), sg.InputText(key='cost', readonly=True)],
#     [sg.Button('Сгенерировать', font=('Arial', 14)), sg.Button('Выход', font=('Arial', 14))],
#     [sg.Image(filename="m_эрудддд.png")]]
# window=sg.Window("Эрудит", layout)
# while True:
#     event, values = window.read()
#     if event in (sg.WINDOW_CLOSED, "Выход"):
#         break
#     if event == "Сгенерировать":
#         a=values["word"]
#         a = a.upper()
#         c=0
#         for i in range(len(a)):
#             for j in dict:
#                 if a[i] in dict[str(j)]:
#                     c += int(j)
#         print(c)
#         window["cost"].update(c)
# window.close()