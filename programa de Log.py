import serial
import keyboard
import time
import datetime

import sys

Tempo_escolhido = int(input("Escolha um tempo em segundos: "))

def ser_avaible():
    
    if ser.is_open:
        
        #if keyboard.read_key() == "enter":
        time.sleep(2.5)
        ser.write("b".encode())

    else:
        print("Não disponivel, tentando novamente")
        ser.open()
        ser_avaible()

ser = serial.Serial("COM3",9600)

ser_avaible()

tempo_inicial = datetime.datetime.now()

tempo = 0

arquivo = open("log.txt", "w")
arquivo.close()

while (ser.isOpen()):
    
    time.sleep(1)

    arquivo = open("log.txt", "a")    
    linha = (ser.readline().decode('utf-8').strip()) + " ; " + (str(datetime.datetime.now().strftime("%H:%M:%S")))
    arquivo.write(linha + "\n")
    arquivo.close()   
    print("Lendo")

    if tempo == Tempo_escolhido:
        ser.write("d".encode())
        ser.close()
        print("Salvo com sucesso")
                
    tempo += 1

    
        

    






