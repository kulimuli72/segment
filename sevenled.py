from gpiozero import LED, Button
from utime import sleep

print("Hello, Pi Pico!")

PUSHB = Button(7)
E = LED(21)
D = LED(20)
C = LED(17)
F = LED(27)
G = LED(26)
A = LED(22)
DP = LED(18)
B = LED(19)

while True:
    if(PUSHB.value()==0):
        E.off()
        D.on()
        C.on()
        F.off()
        G.on()
        B.on()
        A.on()
    else:
        E.on()
        D.on()
        C.on()
        F.on()
        G.on()
        DP.on()
        A.on()
        B.on()
