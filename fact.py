from time import sleep
from pynput.keyboard import Key,Controller

keyboard = Controller()



keyboard.press('s')
   
keyboard.release('s')

keyboard.press('p')
sleep(2)
keyboard.release('p')

keyboard.press('i')
sleep(2)
keyboard.release('i')

keyboard.press('d')
sleep(2)
keyboard.release('d')

keyboard.press('e')
sleep(2)
keyboard.release('e')

keyboard.press('r')
sleep(2)
keyboard.release('r')
