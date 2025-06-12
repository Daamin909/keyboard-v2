import board
import digitalio
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())

macros = Macros()
keyboard.modules.append(macros)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.col_pins = (
    board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
    board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13
)
keyboard.row_pins = (board.GP14, board.GP15, board.GP16, board.GP17, board.GP18)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

encoder_handler.pins = (
    (board.GP19, board.GP20), 
    (board.GP21, board.GP22), 
)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),), 
    ((KC.MPRV, KC.MNXT),), 
]
led_pins = [board.GP26, board.GP27, board.GP28]
led_ios = []
for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False
    led_ios.append(led)

current = 0
def new():
    for i, led in enumerate(led_ios):
        led.value = (i == current)

new()
@macros.add(KC.X) 
def change():
    global current
    current = (current + 1) % 3
    new()

keyboard.keymap = [
    [
        KC.ESC, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC, KC.NO, KC.NO,
        KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.ENT, KC.NO, KC.NO, KC.NO,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.UP, KC.NO, KC.NO, KC.NO,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()
