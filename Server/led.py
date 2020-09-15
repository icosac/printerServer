from gpiozero import LED
from time import sleep

while True:
    try:
        f=open("lock", "r")
        LED(4).on()
    except:
        sleep(1)
