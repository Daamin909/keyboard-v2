# Daamin's keyboard-v2 firmware
# Rev 1.3
# Copyright 2024
# Licensed under zlib license

import board
import busio
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros

# Pin definitions
ROT1A = board.GP19
ROT1B = board.GP20
ROT2A = board.GP22
ROT2B = board.GP21
COL1 = board.GP0
COL2 = board.GP1
COL3 = board.GP2
COL4 = board.GP3
COL5 = board.GP4
COL6 = board.GP5
COL7 = board.GP6
COL8 = board.GP7
COL9 = board.GP8
COL10 = board.GP9
COL11 = board.GP10
COL12 = board.GP11
COL13 = board.GP12
COL14 = board.GP13
ROW1 = board.GP14
ROW2 = board.GP15
ROW3 = board.GP16
ROW4 = board.GP17
ROW5 = board.GP18

# Layer definitions
LAYER_BASE = 0
LAYER_ALT = 1

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
encoder_handler2 = EncoderHandler()
macros = Macros()

keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(MouseKeys())
keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)
keyboard.modules.append(encoder_handler2)
keyboard.modules.append(macros)

# Encoders
encoder_handler.pins = ((ROT1A, ROT1B, None),)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),  # Layer 0: Volume Up / Down
    ((KC.UP, KC.DOWN),),    # Layer 1: Up / Down Arrow
]

encoder_handler2.pins = ((ROT2A, ROT2B, None),)
encoder_handler2.map = [
    ((KC.MRWD, KC.MFFD),),  # Layer 0: Media Rewind / Fast Forward
    ((KC.LEFT, KC.RIGHT),), # Layer 1: Left / Right Arrow
]


keyboard.col_pins = (COL1, COL2, COL3, COL4, COL5, COL6, COL7, COL8, COL9, COL10, COL11, COL12, COL13, COL14)
keyboard.row_pins = (ROW1, ROW2, ROW3, ROW4, ROW5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

numero_uno = KC.TO(LAYER_ALT)
numero_dos = KC.TO(LAYER_BASE)

# LED control pins
led1 = digitalio.DigitalInOut(board.GP26)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP27)
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.GP28)
led3.direction = digitalio.Direction.OUTPUT


led1.value = False
led2.value = False
led3.value = False

# Keymaps
keyboard.keymap = [
    # Layer 0 - Base Layer
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.MUTE,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.NO, KC.MEDIA_PLAY_PAUSE,
        KC.LCTL, KC.LALT, KC.LGUI, KC.SPC,  KC.LGUI, KC.RALT, KC.RCTL, numero_uno,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
    # Layer 1 - Alternate Layer
    [
        KC.GRAVE,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        KC.TAB,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
        KC.CAPS,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.MUTE,
        KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.UP,   KC.RSFT, KC.NO, KC.MEDIA_PLAY_PAUSE,
        KC.LCTL,   KC.LALT, KC.LGUI, KC.SPC,  KC.LEFT, KC.DOWN, KC.RIGHT, numero_dos,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
    ],
]

if __name__ == '__main__':
    keyboard.go()