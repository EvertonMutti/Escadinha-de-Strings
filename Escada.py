# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 10:51:27 2022

@author: Everton SSD
"""

Cont = 0
Frase = input('Digite uma frase ai meu consagrado: ')
TamFrase = len(Frase)

Letra = ''
escadinha = ''

while Cont < TamFrase:
    if Cont == 0:
        Letra = Frase[Cont]
        escadinha += Letra.upper()
    else:
        Letra = Frase[Cont]
        escadinha += Letra
    Cont = Cont + 1
    print(escadinha)

TamFrase = TamFrase - 1
Letra = ''
escadinha = ''
for n in range(TamFrase, -1, -1):
    if n == 0:
        Letra = Frase[n]
        escadinha += Letra.upper()
    else:
        Letra = Frase[n]
        escadinha += Letra
    print(escadinha)
    