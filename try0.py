from pynput.mouse import Button,Controller
from pynput.keyboard import Key
from time import sleep
sleep(10)
mouse=Controller()
mouse.position=(450,850)
mouse.press(Button.left)
mouse.release(Button.left)
sleep(4)
a=' '
from pynput.keyboard import Controller
Keyboard=Controller()
def tyype(a):
    keyboard=Controller()
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

a="$t"        
a='facebook.com'
tyype(a)
sleep(4)
mouse.position=(450,200)
sleep(4)
mouse.press(Button.left)
mouse.release(Button.left)
a="Nithin is THE topper!!"
tyype(a)
from pynput.mouse import Button,Controller
mouse=Controller()
mouse.position=(450,450)
sleep(5)
mouse.press(Button.left)
mouse.release(Button.left)


        
    
    
