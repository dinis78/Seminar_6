import math
import os
from traceback import print_list
from unicodedata import name
from unittest import result
os.system("cls")



# a=int (input('Введите число от 1 до 8 '))
# # if (a>0 and a<6):
# #     print(a, '-> нет')
# # if (a==6 or a==7):   
# #     print(a, '-> да')
# if (a>7 or a<0):
#   print(a, 'не является цыфрой дня недели')





###############################################################

#Старая программа
# x=int(input('Введите число '))
# i=0
# while i<x:
    # def fact(i):
    #     if i==1:
    #         return 1
    #     else:
    #         return i*fact(i-1)
    # i+=1
    # str_fact=str(fact(i))
    # print(str_fact, sep=',', end='')

# Измененная программа ########################
# x=int(input('Введите число '))
# i=0
# while i<x:
#     fact = lambda x: fact(x-1) * x if x > 0 else 1
#     i+=1
#     str_fact=str(fact(i))
#     print(str_fact, sep=',', end='')

#######################################################
########################################################
#Старая программа
# import random
# num=int(input('Введите число '))
# num_list=[]
# for i in range(num):
#    num_list.append(random.randint(1,10))
# print(num_list)
# print(sum(num_list[::2]))  #срез, складываем элементы через один начиная с первого.

# # Измененная программа ########################

# def num (my_list):
#     return [v for i, v in enumerate(my_list, start=1) if  i % 2]
# print (sum(num(num_list)))    


##################################################################
################################################################

text_my = 'самозабвенен мой друг, журнар абвгдейка'
##Старая программа

new_text = text_my.split(' ')
fragment = 'абв'
my_list = []
for new_text in new_text:
   if fragment not in new_text:
     my_list.append(new_text)
print(my_list)     

# # Измененная программа ########################
  

# text_my = list(filter(lambda x: 'абв' not in x, text_my.split()))
# my = " ".join(text_my)
# print(my)  
