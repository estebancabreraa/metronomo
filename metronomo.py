import winsound
import time

soundtime = 10


'''while True:
    winsound.Beep(1000, soundtime)
    time.sleep(delay)
    winsound.Beep(900, soundtime)
    time.sleep(delay)
    winsound.Beep(900, soundtime)
    time.sleep(delay)
    winsound.Beep(900, soundtime)
    time.sleep(delay)'''


menu = '''
################################################################################
#                                  Metronomo                                   #
################################################################################

Metricas:
    1. 2/4
    2. 3/4
    3. 4/4
    4. 5/4
    5. 6/4
    6. 7/4
'''
print(menu)

opcion = input("Ingrese su opcion: ")

opcion2 = input("Desea un 3er timbre para marcar las corcheas? (y/n)")

if opcion == "1":
    tempo = int(input("Ingrese el tempo (bpm):"))
    delay =  60/tempo - (soundtime/100)
    while True:
        winsound.Beep(1000, soundtime)
        print("TAP")
        time.sleep(delay/2)
        winsound.Beep(950, soundtime)
        print("tep")
        time.sleep(delay/2)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay/2)
        winsound.Beep(950, soundtime)
        print("tep")
        time.sleep(delay/2)
elif opcion == "2":
    tempo = int(input("Ingrese el tempo (bpm):"))
    delay =  60/tempo - (soundtime/100)
    while True:
        winsound.Beep(1000, soundtime)
        print("TAP")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
elif opcion == "3":
    tempo = int(input("Ingrese el tempo (bpm):"))
    delay =  60/tempo - (soundtime/100)
    while True:
        winsound.Beep(1000, soundtime)
        print("TAP")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
elif opcion == "4":
    tempo = int(input("Ingrese el tempo (bpm):"))
    delay =  60/tempo - (soundtime/100)
    while True:
        winsound.Beep(1000, soundtime)
        print("TAP")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
elif opcion == "5":
    tempo = int(input("Ingrese el tempo (bpm):"))
    delay =  60/tempo - (soundtime/100)
    while True:
        winsound.Beep(1000, soundtime)
        print("TAP")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
elif opcion == "5":
    tempo = int(input("Ingrese el tempo (bpm):"))
    delay =  60/tempo - (soundtime/100)
    while True:
        winsound.Beep(1000, soundtime)
        print("TAP")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
elif opcion == "6":
    tempo = int(input("Ingrese el tempo (bpm):"))
    delay =  60/tempo - (soundtime/100)
    while True:
        winsound.Beep(1000, soundtime)
        print("TAP")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
        winsound.Beep(900, soundtime)
        print("top")
        time.sleep(delay)
else:
    print("Opcion no valida.")
        



