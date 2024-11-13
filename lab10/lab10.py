# задание 1
# ma=0
# pwin=''
# pma=0
# b=[]
# with open('file4.txt', encoding="UTF-8") as f:
#     for t in f:
#         a=t.split()
#         b.append(a)
#         if int(a[-1])>ma:
#             ma=int(a[-1])
# print(b)
# for j in b:
#     if int(j[-1]) == ma:
#         b.remove(j)
# for l in b:
#     if int(l[-1])>pma:
#         pma=int(l[-1])
#         pwin=l[0]+' '+l[1]
# print(pwin,pma)

# # задание 2
# a=[]
# b=[]
# c='IN'
# with open('file5.txt') as f:
#     for t in f:
#         a.append(t.split())
# for i in range(len(a)):
#     for m in a[i]:
#         if m =='Academy':
#             print('в пятом файле')
# with open('file6.txt') as f1:
#     for t1 in f1:
#         b.append(t1.split())
# for i1 in range(len(b)):
#     for m1 in b[i1]:
#         if m1 =='Academy':
#             print('в шестом файле')

# # задание 3
# a=[]
# e=0
# ne=0
# with open("file4.txt", encoding="UTF-8") as f:
#     for i in f:
#         text=i.split()
#         for j in text:
#             if 'е' in j:
#                 e+=1
#             else:
#                 ne+=1
# print(e/ne*100)

# задание 4
# n=int(input('сколько человек? '))
# g=input('какого пола? ')
# a=[]
# b=[]
# with open('file7.txt', encoding="UTF-8") as f:
#     for i in f:
#         a.append(i.split())
# with open('file8.txt', encoding="UTF-8") as f1:
#     for j in f1:
#         b.append(j.split())
# if g=='ж':
#     for l in range(n):
#         print(a[l][0])
# else:
#     for z in range(n):
#         print(b[(z)][0])

# # задание 5
# a=input('')
# k=0
# with open('filead.txt') as f:
#     l=f.readlines()
# n=len(l)//2
# l.insert(n,a)
# print(l)
# with open('filead.txt', 'w') as f1:
#     f1.writelines(l)

# задание 61
# a=[]
# b=[]
# with open('sypher.txt', encoding="UTF-8") as f:
#     for i in f:
#         a.append(i.split())
# c=''
# for j in range(len(a)):
#     for k in range(len(a[j])):
#         c=str(a[j][k])
#         b.append(c[::-1])
# print(*b)
#задание 62
# a=input()
# a=a[::-1]
# print(a)
# with open('nsypher.txt','w') as f:
#     f.writelines(a)

# задание 7
# import random
# a=[]
# b=[]
# with open('file6.txt') as f:
#     for i in f:
#         a.append(i.split())
# for j in range(len(a)):
#     for k in range(len(a[j])):
#         if len(a[j][k])>=3:
#             b.append(a[j][k].title())
# c=''
# m=random.choice(b)
# c+=m
# b.remove(m)
# c+=random.choice(b)
# b.append(m)
# while len(c)<8 or len(c)>10:
#     c = ''
#     m = random.choice(b)
#     c += m
#     b.remove(m)
#     c += random.choice(b)
#     b.append(m)
# print(c)

# задание 8
# b=input().split()
# n=int(b[0])
# m=int(b[1])
# a=['.']*n
# for i in range(n):
#     a[i]=['.']*m
# l=0
# for j in range(n):
#     for k in range(m):
#         if j%2==0:
#             a[j][k]='#'
#         else:
#             if l%2==0:
#                 a[j][-1]="#"
#             elif l%2==1:
#                 a[j][0]="#"
#     if j%2:
#         l += 1
# for s in range(len(a)):
#     print(*a[s])