from random import randint
from Jogos.interface import *
from Jogos.cores import *


while True:
      jogada = ['Pedra', 'Papel', 'Tesoura']
      r = randint(0, 2)
      cabeçalho('JO KEN PÔ')
      cabeçalho('SELECIONE SUA JOGADA!')
      print(f'SELECIONE {blue()}[0]{semCor()} = {blue()}PEDRA{semCor()}\n'
            f'SELECIONE {blue()}[1]{semCor()} = {blue()}PAPEL{semCor()}\n'
            f'SELECIONE {blue()}[2]{semCor()} = {blue()}TESOURA{semCor()}')
      print(l())
      j = leiaInt('Qual vai ser sua jogada? ')
      while True:
            if j == 0:
                  print(l())
                  break
            elif j == 1:
                  print(l())
                  break
            elif j == 2:
                  print(l())
                  break
            else:
                  print(f'{red()}ERRO!! Digite uma opção válida.{semCor()}')
                  j = leiaInt('Qual vai ser sua jogada? ')
                  continue
      go()
      print(f'O COMPUTADOR JOGOU {blue()}{jogada[r]}{semCor()}')
      print(f'VOCÊ JOGOU {blue()}{jogada[j]}{semCor()}')
      print(l())
      condWin(r, j)
      cond = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
      print(l())
      while cond not in 'SN':
            cabeçalho(f'{red()}ERRO!... Por favor selecione uma opção válida.{semCor()}')
            cond = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
      if cond == 'N':
            print(l())
            print('   Finalizando', end='')
            for c in range(0, 3):
                  print('.', end='')
                  sleep(1)
            print(' Obrigado por jogar! Até logo!')
            print(l())
            break
