# Cyao macropad firmware
# Rev 1.1
# Copyright 2024
# Licensed under zlib license
import board
import busio
import time
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.mouse_keys import MouseKeys


keyboard = KMKKeyboard()

macros = Macros()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(macros)
keyboard.modules.append(MouseKeys())

keyboard.col_pins = (board.D16, board.D17, board.D18, board.D19, board.D20, board.D21, board.D22, board.D26, board.D27, board.D11, board.D12, board.D13, board.D14, board.D10, board.D9, board.D8, board.D3);
keyboard.row_pins = (board.D15, board.D2, board.D1, board.D0, board.D7, board.D6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.ESC , KC.MUTE, KC.VOLD, KC.VOLU, KC.MPRV, KC.MSTP, KC.MNXT, KC.BRID, KC.BRIU, KC.NO  , KC.NO  , KC.NO  , KC.NO  , KC.DEL , KC.NO  , KC.NO  , KC.NO  ,
        KC.GRV , KC.N1  , KC.N2  , KC.N3  , KC.N4  , KC.N5  , KC.N6  , KC.N7  , KC.N8  , KC.N9  , KC.N0  , KC.MINS, KC.EQL , KC.BSPC, KC.NO  , KC.NO  , KC.NO  ,
        KC.TAB , KC.Q   , KC.W   , KC.E   , KC.R   , KC.T   , KC.Y   , KC.U   , KC.I   , KC.O   , KC.P   , KC.LBRC, KC.RBTC, KC.BSLS, KC.NO  , KC.NO  , KC.NO  ,
        KC.ESC , KC.A   , KC.S   , KC.D   , KC.F   , KC.G   , KC.H   , KC.J   , KC.K   , KC.L   , KC.SCLN, KC.QUOT, KC.ENT , KC.NO  , KC.NO  , KC.NO  , KC.NO  ,
        KC.LSFT, KC.Z   , KC.X   , KC.C   , KC.V   , KC.B   , KC.N   , KC.M   , KC.COMM, KC.DOT , KC.SLSH, KC.NO  , KC.NO  , KC.RSFT, KC.NO  , KC.UP  , KC.NO  ,
        KC.LALT, KC.LCMD, KC.LCTL, KC.NO  , KC.NO  , KC.SPC , KC.NO  , KC.NO  , KC.NO  , KC.RCTL, KC.RCMD, KC.MO(1), KC.NO  , KC.NO  , KC.LEFT, KC.DOWN, KC.RGHT, 
    ],
    [
        KC.ESC , KC.F1  , KC.F2  , KC.F3  , KC.F4  , KC.F5  , KC.F6  , KC.F7  , KC.F8  , KC.F9  , KC.F10 , KC.F11 , KC.F12 , KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    ]
]

if __name__ == '__main__':
    keyboard.go()
