from pynput.mouse import Button,Controller
from pynput.keyboard import Key
from time import sleep
from pynput.keyboard import Controller
def tyype(a):
    Keyboard=Controller()
    a=list(a)
    for i in range(0,len(a)):
        if(a[i]=='$'):
            Keyboard.press(Key.ctrl)
            continue
        Keyboard.press(a[i])
        Keyboard.release(a[i])
    Keyboard.release(Key.ctrl)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
i=1
sleep(5)
while(i<=500):
    i+=1
    a = str(i)+".Spam"
    tyype(a)
    sleep(0.5)
