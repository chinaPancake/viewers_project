from pynput import keyboard

import mouse
from pynput.keyboard import Key, Listener, Controller

import keyboard as kb

# Don't do this! This will call `print('space')` immediately then fail when the key is actually pressed.
#keyboard.add_hotkey('space', print('space was pressed'))

#mouse.move(+value go to rigt - value go to left, +value go down - value go up)


def on_press(key):
    try:
        if kb.is_pressed('ctrl + right'):
            mouse.move(30,0, absolute = False)
        if kb.is_pressed('ctrl + left'):
            mouse.move(-29,0, absolute = False)
        if kb.is_pressed('ctrl + down'):
            mouse.move(0,30, absolute = False)
        if kb.is_pressed('ctrl + up'):
            mouse.move(0,-29, absolute = False)
        if kb.is_pressed('shift'):
            mouse.click('right')
        if kb.is_pressed('alt + ctrl'):
            mouse.click('left')
    except AttributeError:
        print('Error')

def on_release(key):
    if key == keyboard.Key.esc:
        print('program closed')
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

