






#print ' om namo narayana'
from pynput.keyboard import Controller,Key
import webbrowser
from time import sleep
webbrowser.open_new('https:/www.facebook.com')
a=Controller()
sleep(6)
def take(b):
    a.press(b)
    a.release(b)
x='p i am sexy, and my friends know it'
for i in range(len(x)):
    take(x[i])
sleep(2)
a.press(Key.ctrl)
a.press(Key.enter)
a.release(Key.enter)
a.release(Key.ctrl)
