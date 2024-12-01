# n=int(input())
# dictionary={'1':[], '2':[], '3':[]}
# for i in range(n):
#     b=input().split()
#     if b[-1]=="woman":
#         dictionary['1'].append(b[0])
#     if b[-1]=="child":
#         dictionary['1'].append(b[0])
#     if b[-1]=="man":
#         dictionary['2'].append(b[0])
#     if b[-1]=="captain":
#         dictionary['3'].append(b[0])
# print(dictionary)
# for j in dictionary:
#     for k in dictionary[j]:
#         print(k)
# print(len(dictionary))

# задание 2
# def cah(b):
#     f=0
#     o=0
#     for mes in b:
#         if mes=="Q":
#             o+=1
#         elif mes =="A":
#             o-=1
#         if o<0:
#             f-=1
#     if f<0 or o!=0:
#         return "-"
#     elif o==0:
#         return "+"
#
# a=input()
# c=[]
# for i in range(len(a)):
#     c.append(a[i])
# print(cah(c))

# # задание 4
# import PySimpleGUI as sg
# layout=[
#     [sg.Text("Перевод числа (-128, 128)", font=("Arial", 19), justification="center")],
#     [sg.Text("Введите число: "), sg.InputText(key='chislo')],
#     [sg.Text("Прямой код: "), sg.InputText(key='pr')],
#     [sg.Text("Обратный: "), sg.InputText(key='ob')],
#     [sg.Text("Дополнительный: "), sg.InputText(key='dop')],
#     [sg.Button('Сгенерировать', font=('Arial', 14))]
#
# ]
#
# window=sg.Window("Перевод числа", layout)
# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     if event == "Сгенерировать":
#         a=int(values["chislo"])
#         b = format(a & 0xFF, '08b')
#         c = format(~a & 0xFF, '08b')
#         d = format((~a + 1) & 0xFF, '08b')
#         window["pr"].update(b)
#         window['ob'].update(c)
#         window['dop'].update(d)
# window.close()