# # # задание 1
#
# def func(x):
#     return x**2/(10+x**3)
# a=-2
# b=5
# n=1000
# le=(b-a)/n
# f=[]
# i=a
# while i<b:
#     f.append(func(i))
#     i+=le
# s=0
# for i in range(0,len(f)-1):
#     s+=le/2*(f[i]+f[i+1])
# print(s)

# # задание 2
# from random import *
# def sq(a):
#     m=15
#     for i in a:
#         if sum(i)!=m:
#             return 0
#     if a[0][2]+a[1][2]+a[2][2]==a[0][1]+a[1][1]+a[2][1]==a[0][0]+a[1][0]+a[2][0]==sum(a[0])==sum(a[1])==sum(a[2])==a[0][0]+a[1][1]+a[2][2]==a[0][2]+a[1][1]+a[2][0]==m:
#         return 1
#     else:
#         return 0
# def rsq():
#     rand,a= list(range(1, 10)),[]
#     shuffle(rand)
#     for i in range(0, 9, 3):
#         a.append(rand[i:i + 3])
#     return a
# n = 3
# a = rsq()
# while not(sq(a)):
#     a = rsq()
# else:
#     for j in range(3):
#         for k in range(3):
#             print(a[j][k], end= ' ')
#         print()

# # задние 3
# print('количество сокровищ')
# n=int(input())
# a=[]
# print('координаты сокровищ')
# for i in range(n):
#     cord=input()
#     a.append(cord.split(' '))
# print('координаты александра')
# name=input().split(' ')
# minim=100000
# mi=[]
# for j in range(n):
#     if ((int(a[j][0])-int(name[0]))**2+(int(a[j][1])-int(name[1]))**2)**0.5<=minim:
#         minim=((int(a[j][0])-int(name[0]))**2+(int(a[j][1])-int(name[1]))**2)
#         mi=[a[j][0], a[j][1]]
#
# print(mi)

# # задание 4
#
# menu = [
# ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
# ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
# ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
# ]
# print("""введите что вы хотите сделать с помощью числа.
#         1-отобразить меню ресторана
#         2-Найти блюдо по названию и отобразить его ингредиенты и цену. (Вы вводите название блюда)
#         3-Добавить новое блюдо в меню
#         4-Изменить цену блюда (Вы вводите название и новую цену)""")
# a=int(input())
# if a==1:
#     print(menu)
# elif a==2:
#     b=input("название: \n")
#     for i in range(len(menu)):
#         if menu[i][0]==b:
#             print(menu[i][1:])
# elif a==3:
#     c=input("добавьте новое блюдо, введите через | пример: название|ингридиенты|цена \n")
#     menu.append(c.split("|"))
#     print(menu)
# elif a==4:
#     d=input("какую цену блюда изменить? (название): \n")
#     e=input("введите новую цену: \n")
#     for j in range(len(menu)):
#         if menu[j][0]==d:
#             menu[j][-1]=e
#     print(menu)

# # задание 5
#
# n=int(input())
# matrix=[]
# trmatrix=matrix
# # for m in range(n):
# #     trmatrix[m]=[0]*n
# for i in range(n):
#     b=input()
#     matrix.append(b.split(' '))
# for j in range(n):
#     k=matrix[j][j]
#     trmatrix[j][j]=(matrix[n-j-1][j])
#     trmatrix[n-j-1][j]=k
#
# for l in range(n):
#     for p in range(n):
#         print(trmatrix[l][p], end=' ')
#     print()



# # задание 7
# print('размеры')
# a = input().split(' ')
# matr=[]
# print('места')
# for i in range(int(a[0])):
#     b=input()
#     matr.append(b.split(' '))
# print("компания")
# comp=int(input())
# c="0"*comp
# k=0
# for j in range(int(a[0])):
#     if c in ''.join(matr[j]):
#         print("номер ряда:", j+1)
#         k+=1
#         break
# if k==0:
#     print('0')

# задание 8
#
# a=input().split(' ')
# matr=[0]*int(a[0])
# for k in range(int(a[0])):
#     matr[k]=[0]*int(a[1])
# print(matr)
# for i in range(int(a[0])):
#     for j in range(int(a[1])):
#         if j==0 or i ==0:
#             matr[i][j]=1
#         else:
#             matr[i][j]=matr[i-1][j]+matr[i][j-1]
# for x in range(int(a[0])):
#     for y in range(int(a[1])):
#         print(matr[x][y],' '*(4 - len(str(matr[x][y]))), end= ' ')
#     print()


# # задание 9
# import random
# a=["*"]*4
# cor=[]
# for i in range(4):
#     a[i]=["*"]*4
# for j in range(4):
#     for k in range(4):
#         cor.append([str(j),str(k)])
# q=[]
# for o in range(5):
#     t=random.choice(cor)
#     q.append(t)
#     cor.remove(t)
# print(q)
# b=0
# while b<4:
#     x=input("координаты: ").split(",")
#     if x==q[0] or x==q[1] or x ==q[2] or x==q[3]:
#         a[int(x[0])][int(x[1])] = '0'
#         print("popal")
#         b+=1
#         g=q.index(x)
#         q[g]=1000
#     elif x==q[4]:
#         print("bombaaa")
#         b+=5
#     else:
#         a[int(x[0])][int(x[1])] = '.'
#         print("promax")
#     for z in range(4):
#         for v in range(4):
#             print(a[z][v], end=' ')
#         print()
# if b==4:
#     print('congrats you!')




