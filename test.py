# sudo pip install evdev

from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event4')

b = 290
y = 291
x = 288
a = 289
lt = 292
rt = 293
select = 296
start = 297

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        keyevent = categorize(event)
        if keyevent.keystate == KeyEvent.key_down:
            if keyevent.scancode == b:
                print('B')
            elif keyevent.scancode == y:
                print('Y')
            elif keyevent.scancode == x:
                print('X')
            elif keyevent.scancode == a:
                print('A')
            elif keyevent.scancode == lt:
                print('LT')
            elif keyevent.scancode == rt:
                print('RT')
            elif keyevent.scancode == select:
                print('SELECT')
            elif keyevent.scancode == start:
                print('START')
    if event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        print absevent