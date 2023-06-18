# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

def division(a):
    print(a)
    if len(a) == 1:
        return
    else:
        num = list(a)
        r = num[-1]
        q = a[:-1]
        value = int(q)*3 + int(r)
        division(str(value))
a = input()
division(a)