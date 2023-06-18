# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
#
from math import sqrt
n, k = map(int, (x for x in input().split()))

pos_k  = sqrt(k)
max_pos = 2*n
alice = (max_pos-pos_k+1)*(max_pos-pos_k+1)
print(int(alice))