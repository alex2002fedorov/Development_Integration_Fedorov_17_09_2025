from sympy import *
k, T, C, L = symbols('k T C L')
#1 способ
C_ost = 120000 # поменял правильно молодец
Am_lst = []
C_ost_lst = []
for i in range(10):
  Am = (C-L)/T
  C_ost -=Am.subs({C:120000, T:10, L:0}) # поменял правильно молодец
  Am_lst.append(round(Am.subs({C:120000, T:10, L:0}),2)) # поменял правильно молодец
  C_ost_lst.append(round(C_ost,2))
print("Am_lst:" , Am_lst) #Что это означает? # выводит список значений амортизации #Оценка:5
print("C_ost_lst:" , C_ost_lst)
print('******')

#2 способ
Aj = 0
C_ost = 120000
Am_lst_2 = []
C_ost_lst_2 = []

for i in range(10):
    Am = k * 1/T * (C - Aj)
    C_ost -= Am.subs({C: 120000, T: 10, k: 2})
    Am_lst_2.append(round(Am.subs({C: 120000, T: 10, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)
print('******')

#Контейнер табличного вывода
import pandas as pd
Y = range(1, 11)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2']) #Что это означает? # присваивает значения в таблицу #Оценка:5

print(tfame)
print(tfame2)
print('******')

# Контейнер визуализации
from matplotlib import pyplot as plt #Что это означает? # импортирует библиотеку для визуализации #Оценка:5

#plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
#plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
#plt.show()

#vals = Am_lst
#labels = list(range(1, 11))
#explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

#fig, ax = plt.subplots()
#ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'linewidth': 1, 'edgecolor': 'k'}, rotatelabels=True)
#ax.axis('equal')
#plt.show()

#vals = Am_lst_2
#labels = list(range(1, 11))
#explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

#fig, ax = plt.subplots()
#ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'linewidth': 1, 'edgecolor': 'k'}, rotatelabels=True)
#ax.axis('equal')
#plt.show()

# 2 вариант
print();
print('*** 2 вариант ***')
from sympy import *
k, T, C, L = symbols('k T C L')
#1 способ
C_ost = 120000
Am_lst = []
C_ost_lst = []
for i in range(9):
  Am = (C-L)/T
  C_ost -=Am.subs({C:120000, T:10, L:0})
  Am_lst.append(round(Am.subs({C:120000, T:10, L:0}),2))
  C_ost_lst.append(round(C_ost,2))
print("Am_lst:" , Am_lst)
print("C_ost_lst:" , C_ost_lst)
print('******')

#2 способ
Aj = 0
C_ost = 120000
Am_lst_2 = []
C_ost_lst_2 = []

for i in range(10):
    Am = k * 1/T * (C - Aj)
    C_ost -= Am.subs({C: 120000, T: 10, k: 2})
    Am_lst_2.append(round(Am.subs({C: 120000, T: 10, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))

print('Am_lst_2:', Am_lst_2)
print('C_ost_lst_2:', C_ost_lst_2)
print('******')

#Контейнер табличного вывода
import pandas as pd
Y = range(1, 11)
table1 = list(zip(Y, C_ost_lst, Am_lst))
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=['Y', 'C_ost_lst', 'Am_lst'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_lst_2', 'Am_lst_2'])

print(tfame)
print(tfame2)
print('******')

# Контейнер визуализации
from matplotlib import pyplot as plt

#plt.plot(tfame['Y'], tfame['C_ost_lst'], label='Am')
#plt.plot(tfame2['Y'], tfame2['C_ost_lst_2'], label='Am_2')
#plt.show()

#vals = Am_lst
#labels = list(range(1, 11))
#explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

#fig, ax = plt.subplots()
#ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'linewidth': 1, 'edgecolor': 'k'}, rotatelabels=True)
#ax.axis('equal')
#plt.show()

#vals = Am_lst_2
#labels = list(range(1, 11))
#explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

#fig, ax = plt.subplots()
#ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'linewidth': 1, #'edgecolor': 'k'}, rotatelabels=True)
#ax.axis('equal')
#plt.show()

import os
secret = os.environ.get('Fedorov_17_09_2025_1')
print(secret)
print('******')

secret_anton1 = os.environ.get('Fedorov_17_09_2025_1')
secret_anton2 = os.environ.get('Fedorov_17_09_2025_2')
secret_anton3 = os.environ.get('Fedorov_17_09_2025_3')
print(secret_anton1, secret_anton2, secret_anton3)
print('******')
