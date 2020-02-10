from playsound import playsound
modo = 0
musica = 0
print('Bem vindo ao midea player!!')
print('Escolha um metodo do player: ')
print('1 - tocar musica especifica: ')
print('2 - tocar musica na sequência: ')
print('3 - tocar musicas de forma aleatoria: ')
modo = int(input('Digite um valor valido e inteiro de 1 a 3: '))
if modo == 1:
    print('Escolha uma musica: ')
    print('1 - stresse out')
    print('2 - bonde do tigrão')
    print('3 - numb encore')
    musica = int(input('Digite um valor valido e inteiro de 1 a 3: '))
    if musica == 1:
        playsound('musica.mp3')
    if musica == 2:
        playsound('musica.mp3')
    if musica == 3:
        playsound('musica.mp3')
if modo == 2:
    print('Sequência:')
    print('1 - stresse out')
    print('2 - bonde do tigrão')
    print('3 - numb encore')
    playsound('musica.mp3')
    playsound('musica.mp3')
    playsound('musica.mp3')
if modo == 3:
    playsound('musica.mp3')