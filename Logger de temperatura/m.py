from pynput import keyboard
import time

# variável para controlar a execução
stop_acquisition = False

# função chamada quando uma tecla é pressionada
def on_press(key):
    global stop_acquisition
    try:
        if key.char == 'q':  # se a tecla 'q' for pressionada
            stop_acquisition = True
            print("a tecla 'q' foi pressionada. parando a aquisição...")
            return False  # encerra o listener
    except AttributeError:
        pass

# loop principal para aquisição de dados
print("iniciando a aquisição de dados. pressione 'q' para parar.")
while not stop_acquisition:
    # simulação de aquisição de dados
    print("adquirindo dados...")
    time.sleep(1)  # simula um intervalo entre coletas

    # inicia o listener de teclado no loop
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

print("aquisição de dados finalizada.")
