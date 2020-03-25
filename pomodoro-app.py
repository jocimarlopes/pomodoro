import time
import sys

play = 0

while play == 0:
    print("APLICAÇÃO SEM SOM (BETA)")
    time.sleep(1)
    print("Versão: 0.2")
    time.sleep(1)
    counter = 1

    while counter < 4:
        input("Pressione ENTER para iniciar 25 minutos..")
        time.sleep(1)
        print('Pomodori (25 minutos) a partir de agora!')
        time.sleep(1500)
        time.sleep(1)
        print('Pausa curta (05 minutos)')
        time.sleep(1)
        input('Pressione enter para iniciar a Pausa Curta..')
        time.sleep(300)
        counter = counter + 1
    else:
        print('Pausa Longa (15 minutos)')
        input('Pressione ENTER para iniciar a Pausa Longa..')
        time.sleep(300)
        time.sleep(600)
else:
    print("Finalizando...")
    time.sleep(2)
    sys.exit()
