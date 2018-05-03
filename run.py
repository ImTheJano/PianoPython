"""
 * By: Alejandro G (Jano)
 * 03/05/2018
 * github.com/imthejano
 * facebook.com/imthejano
 * twitter.com/imthejano
"""
import serial
import sys
import threading
import _thread
sys.path.append('./Wave.py')
from Wave import WavePack

serAvailable=0
packLoaded=0

def checkPort():
    try:
        ser = serial.Serial(port, 115200)
        serAvailable=1
    except:
        print ("Serial port is not available, use keyboard")
        serAvailable=0

def play(n):
    pianoPack.play(notes[n])

def waitForKey():
    while(1):
        checkPort()
        aux=""
        print("press a key...")
        if (serAvailable):
            aux=ser.read()
        else:
            aux=input()
        print (aux)
        t = threading.Thread(target=play, args=(aux,))
        t.start()

port=input("in port: ")        
notes={"a"or b'a':1,"b"or b'b':2,"c"or b'c':3,"d"or b'd':4,"e"or b'e':5,
       "f"or b'f':6,"g"or b'g':7,"h"or b'h':8,"i"or b'i':9,"j"or b'j':10,
       "k"or b'k':11,"l"or b'l':12,"m"or b'm':13,"n"or b'n':14,"o"or b'o':15,
       "p"or b'p':16,"q"or b'q':17,"r"or b'r':18,"s"or b's':19,"t"or b't':20,
       "u"or b'u':21,"v"or b'v':22,"w"or b'w':23,"x"or b'x':24}

while (not packLoaded):
    try:
        pack=input("pack path: ")
        packLoaded=1
        pianoPack=WavePack(100000,pack,"piano",25)
        pianoPack.loadPack()
    except:
        packLoaded=0
        print ("pack not found")

waitForKey()

        

