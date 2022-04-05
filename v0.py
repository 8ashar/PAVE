# sudo pip install evdev

from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event4')

for event in gamepad.read_loop():
    keyevent = categorize(event)
    print(keyevent)
    print('\n')