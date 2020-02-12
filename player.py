from playsound import playsound
from random import shuffle
modo = 0
playlist = ['musica 1.mp3', 'musica 2.mp3', 'musica 3.mp3']
musica = 0
print('Bem vindo ao midea player!!')
print('Escolha um metodo do player: ')
print('1 - Twenty One Pilots: Stressd Out. ')
print('2 - MC Leandrinho: Bonde do Tigrão. ')
print('3 - Linkin Park: Numb Encore. ')
print('0 - Tocar uma musica aleatoria.')

modo = int(input('Digite um valor valido e inteiro de 0 a 3: '))
if modo == 1:
    print('Play Twenty one pilots: Stressd Out...')
    playsound(playlist[0])
else:
    if modo == 2:
        print('Play MC Leandrinho: Bonde do tigrão...')
        playsound(playlist[1])
    else:
        if modo == 3:
            print('Play Linkin Park: Numb Encore...')
            playsound(playlist[2])
        else:
            if modo == 0:
                print('Musica elatoria...')
                shuffle(playlist)
                playsound(playlist[0])
            else:
                print('\33[1:31mMODO INVALIDO!')