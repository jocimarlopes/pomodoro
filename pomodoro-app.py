import winsound
import time
import sys
import tkinter as tk

frequency = 500
duration = 10000
play = input("Deseja iniciar?")

while play in 'sim Sim SIM YES yes Yes':
    input("Pressione ENTER para iniciar 25 minutos..")

    counter = 1

    while counter < 4:
        time.sleep(1)
        print('Pomodori (25 minutos) a partir de agora!')
        time.sleep(1500)
        winsound.Beep(600, 5000)
        time.sleep(1)
        print('Pausa curta (05 minutos)')
        time.sleep(1)
        input('Pressione enter para Começar')
        time.sleep(300)
        counter = counter + 1
    else:
        time.sleep(300)
        time.sleep(600)
else:
    print("Finalizando...")
    time.sleep(2)
    sys.exit()