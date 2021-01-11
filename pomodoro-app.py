import time
import sys
import os



play = 0

duration = 3 #segundos
freq = 1440 #Hz

while play == 0:
    print("APLICAÇÃO P/ LINUX (BETA)")
    time.sleep(1)
    print("Versão: 0.5")
    time.sleep(1)
    counter = 1

    while counter < 4:
        input("Pressione ENTER para iniciar 25 minutos..")
        time.sleep(1)
        print('Pomodori (25 minutos) a partir de agora!')
        time.sleep(1500)
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        time.sleep(1)
        print('Pausa curta (05 minutos)')
        time.sleep(1)
        input('Pressione enter para iniciar a Pausa Curta..')
        time.sleep(300)
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
        counter = counter + 1
    else:
        print('Pausa Longa (15 minutos)')
        input('Pressione ENTER para iniciar a Pausa Longa..')
        time.sleep(900)
        os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
else:
    print("Finalizando...")
    time.sleep(2)
    sys.exit()
