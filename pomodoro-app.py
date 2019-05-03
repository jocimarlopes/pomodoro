import winsound
import time
import sys
import tkinter as tk

frequency = 500
duration = 10000
play = 0

while play == 0:
    counter = 1

    while counter < 4:
        input("Pressione ENTER para iniciar 25 minutos..")
        time.sleep(1)
        print('Pomodori (25 minutos) a partir de agora!')
        time.sleep(1500)
        winsound.Beep(600, 5000)
        time.sleep(1)
        print('Pausa curta (05 minutos)')
        time.sleep(1)
        input('Pressione enter para iniciar a Pausa Curta..')
        time.sleep(300)
        winsound.Beep(600, 5000)
        counter = counter + 1
    else:
        print('Pausa Longa (15 minutos)')
        input('Pressione ENTER para iniciar a Pausa Longa..')
        time.sleep(300)
        time.sleep(600)
        winsound.Beep(600, 5000)
else:
    print("Finalizando...")
    time.sleep(2)
    sys.exit()
