#Jogo do número secreto
import random

print('''
░░░░░██╗░█████╗░░██████╗░░█████╗░  ██████╗░░█████╗░  ███╗░░██╗██╗░░░██╗███╗░░░███╗███████╗██████╗░░█████╗░
░░░░░██║██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔══██╗  ████╗░██║██║░░░██║████╗░████║██╔════╝██╔══██╗██╔══██╗
░░░░░██║██║░░██║██║░░██╗░██║░░██║  ██║░░██║██║░░██║  ██╔██╗██║██║░░░██║██╔████╔██║█████╗░░██████╔╝██║░░██║
██╗░░██║██║░░██║██║░░╚██╗██║░░██║  ██║░░██║██║░░██║  ██║╚████║██║░░░██║██║╚██╔╝██║██╔══╝░░██╔══██╗██║░░██║
╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝  ██████╔╝╚█████╔╝  ██║░╚███║╚██████╔╝██║░╚═╝░██║███████╗██║░░██║╚█████╔╝
░╚════╝░░╚════╝░░╚═════╝░░╚════╝░  ╚═════╝░░╚════╝░  ╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░

░██████╗███████╗░█████╗░██████╗░███████╗████████╗░█████╗░
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
╚█████╗░█████╗░░██║░░╚═╝██████╔╝█████╗░░░░░██║░░░██║░░██║
░╚═══██╗██╔══╝░░██║░░██╗██╔══██╗██╔══╝░░░░░██║░░░██║░░██║
██████╔╝███████╗╚█████╔╝██║░░██║███████╗░░░██║░░░╚█████╔╝
╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚════╝
''')
print('''
V̳o̳c̳ê̳  t̳e̳m̳  1̳0̳  t̳e̳n̳t̳a̳t̳i̳v̳a̳s̳  p̳a̳r̳a̳  a̳c̳e̳r̳t̳a̳r̳  o̳  n̳ú̳m̳e̳r̳o  s̳e̳c̳r̳e̳t̳o̳  e̳n̳t̳r̳e  1̳0̳0̳0̳  e̳  9̳9̳9̳9̳.̳
A̳  p̳a̳r̳t̳i̳r̳  d̳a̳  5̳º̳  t̳e̳n̳t̳a̳t̳i̳v̳a̳  o̳  j̳o̳g̳o̳  i̳r̳á̳  t̳e̳  a̳j̳u̳d̳a̳r̳,̳  d̳a̳n̳d̳o̳  d̳i̳c̳a̳s̳!̳
''')
input('<<< Tecle Algo Para Continuar! >>>')

numero_secreto = random.randint(1000, 9999)

x = (numero_secreto // 1000)
y = (numero_secreto // 100 - (numero_secreto // 100 - (numero_secreto % 1000))) // 100
z = (numero_secreto // 10) % 10
w = numero_secreto % 10

print(x,y,z,w)

primeiro_digito = '_'
segundo_digito = '_'
terceiro_digito = '_'
quarto_digito = '_'

tentativas = 0
dicas = 1

for i in range(1, 10):
    chute = int(input(f'\nDigite seu chute: '))

    if chute < 1000: 
        print("Número inválido! Digite somente números entre 1000 a 9999")
    elif chute > 9999:
        print("número inválido! Digite somente números entre 1000 a 9999")
    else:
        a = (chute // 1000)
        b = (chute // 100 - (chute // 100 - (chute % 1000))) // 100
        c = (chute // 10) % 10
        d = chute % 10
        
        if chute == numero_secreto:
            print(f'Você acertou o número secreto!!\nNúmero de tentativas: {tentativas}')
            primeiro_digito = a
            segundo_digito = b
            terceiro_digito = c
            quarto_digito = d
            print(f'Número secreto: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')

            break
        else:
            if a != x:
                if b!= y:
                    if c != z:
                        if d != w:
                            print(f'Você não acertou nenhum digito dessa vez 😓\n\nTente Novamente! Você ainda tem {10 - tentativas} tentativas.\n')
        if a == x:
            primeiro_digito = a
            print(f'Você acertou o primeiro digito (👍 ͡❛ _> ͡❛)👍!')
        if b == y:
            segundo_digito = b
            print(f'Você acertou o segundo digito (👍 ͡❛ _> ͡❛)👍!')
        if c == z:
            terceiro_digito = c
            print(f'Você acertou o terceiro digito (👍 ͡❛ _> ͡❛)👍!')
        if d == w:
            quarto_digito = d
            print(f'Você acertou o quarto digito (👍 ͡❛ _> ͡❛)👍!')
        tentativas += 1
        print(f'faltam {10-tentativas} tentativas')

        if tentativas >= 2:
            print(f'\n\nVou te dar uma díca!!')
            
            if a == x:
                dicas = 1
            elif primeiro_digito == 'PAR' or primeiro_digito == 'ÍMPAR':
                if a > x:
                    primeiro_digito = f'<{a}'
                else: 
                    primeiro_digito = f'>{a}'
            if b == y:
                dicas = 1
            elif segundo_digito == 'PAR' or segundo_digito == 'ÍMPAR':
                if b > y:
                    segundo_digito = f'<{b}'
                else:
                    segundo_digito = f'>{b}'
            if c == z:
                dicas = 1
            elif terceiro_digito == 'PAR' or terceiro_digito == 'ÍMPAR':
                if c > z:
                    terceiro_digito = f'<{c}'
                else:
                    terceiro_digito = f'>{c}'
            if d == w:
                dicas = 1
            elif quarto_digito == 'PAR' or quarto_digito == 'ÍMPAR':
                if d > w:
                    quarto_digito = f'<{d}'
                else:
                    quarto_digito = f'>{d}'

            if dicas == 1:
                if a != x:
                    if x % 2 == 0:
                        print(f'==> O primeiro digito é par!')
                        primeiro_digito = 'PAR'
                    else:
                        print(f'==> O primeiro digito é ímpar!')
                        primeiro_digito = 'ÍMPAR'
                elif b!= y:
                    if y % 2 == 0:
                        print(f'==> O segundo digito é par!')
                        segundo_digito = 'PAR'
                    else:
                        print(f'==> O segundo digito é ímpar!')
                        segundo_digito = 'ÍMPAR'
                elif c != z:
                    if z % 2 == 0:
                        print(f'==> O terceiro digito é par!')
                        terceiro_digito = 'PAR'
                    else:
                        print(f'==> O terceiro digito é ímpar!')
                        terceiro_digito = 'ÍMPAR'
                elif d != w:
                    if w % 2 == 0:
                        print(f'==> O quarto digito é par!')
                        quarto_digito = 'PAR'
                    else:
                        print(f'==> O quarto digito é ímpar!')
                        quarto_digito = 'ÍMPAR'
            dicas -= 1

        if tentativas > 10:
            print('Número de tentativas foi exedido!!!')

        print(f'\nSeu código é: {primeiro_digito} {segundo_digito} {terceiro_digito} {quarto_digito}')