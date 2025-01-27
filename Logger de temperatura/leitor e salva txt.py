import serial
import keyboard
import time
import datetime
from pynput import keyboard
import sys


def end():
    ser.close()
    f.close()
    print("Salvo com sucesso")

def ser_avaible():
    
    if ser.is_open:
        print("Começando Leitura")
        time.sleep(2.5)
        ser.write("b".encode())
    else:
        print("Não disponivel, tentand novamente")
        ser.open()
        ser_avaible()

ser = serial.Serial("COM3",9600)

ser_avaible()

f = open("log.txt", "w")

tempo_inicial = datetime.datetime.now()

tempo = 0

while (ser.isOpen()):
    try:
        tempo_final = datetime.datetime.now()
        linha = (ser.readline().decode('utf-8').strip()) + " ; " + (str(datetime.datetime.now().strftime("%H:%M:%S")))
        f.writelines(linha + "\n")

    
        print("Lendo")

        if tempo >= 10:
            ser.write("d".encode())
            end()
            
        tempo += 1

        time.sleep(1)
    except:
        f.close()
    
        




