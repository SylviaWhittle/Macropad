# MACROPAD Hotkeys example: Firefox web browser for Linux

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                       # REQUIRED dict, must be named 'app'
    'name' : 'Notion', # Application name
    'macros' : [              # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x00ffff, 'Head 1', ['/', 'h1', Keycode.ENTER]),
        (0x00ffff, 'Head 2', ['/', 'h2', Keycode.ENTER]),
        (0x00ffff, 'Head 3', ['/', 'h3', Keycode.ENTER]),
        # 2nd row ----------
        (0xffffff, 'White', ['/', 'col white', Keycode.ENTER]),
        (0xff0000, 'Red', ['/', 'col red', Keycode.ENTER]),
        (0xff4400, 'Orange', ['/', 'col orange', Keycode.ENTER]),
        # 3rd row ----------
        (0xffff00, 'Yellow', ['/', 'col yellow', Keycode.ENTER]),
        (0x0000ff, 'Blue', ['/', 'col blue', Keycode.ENTER]),
        (0xff00ff, 'Pink', ['/', 'col pink', Keycode.ENTER]),
        # 4th row ----------
        (0x00ffff, '----', []),
        (0x00ffff, '----', []),
        (0x00ffff, '----', []),
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close window/tab
    ]
}
