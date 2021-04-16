# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2008 Alex Holkner
# Copyright (c) 2008-2021 pyglet contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

"""Event constants from /usr/include/linux/input.h """


EV_SYN = 0x00
EV_KEY = 0x01
EV_REL = 0x02
EV_ABS = 0x03
EV_MSC = 0x04
EV_LED = 0x11
EV_SND = 0x12
EV_REP = 0x14
EV_FF = 0x15
EV_PWR = 0x16
EV_FF_STATUS = 0x17
EV_MAX = 0x1f

# Synchronization events.

SYN_REPORT = 0
SYN_CONFIG = 1

# Keys and buttons

KEY_RESERVED = 0
KEY_ESC = 1
KEY_1 = 2
KEY_2 = 3
KEY_3 = 4
KEY_4 = 5
KEY_5 = 6
KEY_6 = 7
KEY_7 = 8
KEY_8 = 9
KEY_9 = 10
KEY_0 = 11
KEY_MINUS = 12
KEY_EQUAL = 13
KEY_BACKSPACE = 14
KEY_TAB = 15
KEY_Q = 16
KEY_W = 17
KEY_E = 18
KEY_R = 19
KEY_T = 20
KEY_Y = 21
KEY_U = 22
KEY_I = 23
KEY_O = 24
KEY_P = 25
KEY_LEFTBRACE = 26
KEY_RIGHTBRACE = 27
KEY_ENTER = 28
KEY_LEFTCTRL = 29
KEY_A = 30
KEY_S = 31
KEY_D = 32
KEY_F = 33
KEY_G = 34
KEY_H = 35
KEY_J = 36
KEY_K = 37
KEY_L = 38
KEY_SEMICOLON = 39
KEY_APOSTROPHE = 40
KEY_GRAVE = 41
KEY_LEFTSHIFT = 42
KEY_BACKSLASH = 43
KEY_Z = 44
KEY_X = 45
KEY_C = 46
KEY_V = 47
KEY_B = 48
KEY_N = 49
KEY_M = 50
KEY_COMMA = 51
KEY_DOT = 52
KEY_SLASH = 53
KEY_RIGHTSHIFT = 54
KEY_KPASTERISK = 55
KEY_LEFTALT = 56
KEY_SPACE = 57
KEY_CAPSLOCK = 58
KEY_F1 = 59
KEY_F2 = 60
KEY_F3 = 61
KEY_F4 = 62
KEY_F5 = 63
KEY_F6 = 64
KEY_F7 = 65
KEY_F8 = 66
KEY_F9 = 67
KEY_F10 = 68
KEY_NUMLOCK = 69
KEY_SCROLLLOCK = 70
KEY_KP7 = 71
KEY_KP8 = 72
KEY_KP9 = 73
KEY_KPMINUS = 74
KEY_KP4 = 75
KEY_KP5 = 76
KEY_KP6 = 77
KEY_KPPLUS = 78
KEY_KP1 = 79
KEY_KP2 = 80
KEY_KP3 = 81
KEY_KP0 = 82
KEY_KPDOT = 83

KEY_ZENKAKUHANKAKU = 85
KEY_102ND = 86
KEY_F11 = 87
KEY_F12 = 88
KEY_RO = 89
KEY_KATAKANA = 90
KEY_HIRAGANA = 91
KEY_HENKAN = 92
KEY_KATAKANAHIRAGANA = 93
KEY_MUHENKAN = 94
KEY_KPJPCOMMA = 95
KEY_KPENTER = 96
KEY_RIGHTCTRL = 97
KEY_KPSLASH = 98
KEY_SYSRQ = 99
KEY_RIGHTALT = 100
KEY_LINEFEED = 101
KEY_HOME = 102
KEY_UP = 103
KEY_PAGEUP = 104
KEY_LEFT = 105
KEY_RIGHT = 106
KEY_END = 107
KEY_DOWN = 108
KEY_PAGEDOWN = 109
KEY_INSERT = 110
KEY_DELETE = 111
KEY_MACRO = 112
KEY_MUTE = 113
KEY_VOLUMEDOWN = 114
KEY_VOLUMEUP = 115
KEY_POWER = 116
KEY_KPEQUAL = 117
KEY_KPPLUSMINUS = 118
KEY_PAUSE = 119

KEY_KPCOMMA = 121
KEY_HANGUEL = 122
KEY_HANJA = 123
KEY_YEN = 124
KEY_LEFTMETA = 125
KEY_RIGHTMETA = 126
KEY_COMPOSE = 127

KEY_STOP = 128
KEY_AGAIN = 129
KEY_PROPS = 130
KEY_UNDO = 131
KEY_FRONT = 132
KEY_COPY = 133
KEY_OPEN = 134
KEY_PASTE = 135
KEY_FIND = 136
KEY_CUT = 137
KEY_HELP = 138
KEY_MENU = 139
KEY_CALC = 140
KEY_SETUP = 141
KEY_SLEEP = 142
KEY_WAKEUP = 143
KEY_FILE = 144
KEY_SENDFILE = 145
KEY_DELETEFILE = 146
KEY_XFER = 147
KEY_PROG1 = 148
KEY_PROG2 = 149
KEY_WWW = 150
KEY_MSDOS = 151
KEY_COFFEE = 152
KEY_DIRECTION = 153
KEY_CYCLEWINDOWS = 154
KEY_MAIL = 155
KEY_BOOKMARKS = 156
KEY_COMPUTER = 157
KEY_BACK = 158
KEY_FORWARD = 159
KEY_CLOSECD = 160
KEY_EJECTCD = 161
KEY_EJECTCLOSECD = 162
KEY_NEXTSONG = 163
KEY_PLAYPAUSE = 164
KEY_PREVIOUSSONG = 165
KEY_STOPCD = 166
KEY_RECORD = 167
KEY_REWIND = 168
KEY_PHONE = 169
KEY_ISO = 170
KEY_CONFIG = 171
KEY_HOMEPAGE = 172
KEY_REFRESH = 173
KEY_EXIT = 174
KEY_MOVE = 175
KEY_EDIT = 176
KEY_SCROLLUP = 177
KEY_SCROLLDOWN = 178
KEY_KPLEFTPAREN = 179
KEY_KPRIGHTPAREN = 180

KEY_F13 = 183
KEY_F14 = 184
KEY_F15 = 185
KEY_F16 = 186
KEY_F17 = 187
KEY_F18 = 188
KEY_F19 = 189
KEY_F20 = 190
KEY_F21 = 191
KEY_F22 = 192
KEY_F23 = 193
KEY_F24 = 194

KEY_PLAYCD = 200
KEY_PAUSECD = 201
KEY_PROG3 = 202
KEY_PROG4 = 203
KEY_SUSPEND = 205
KEY_CLOSE = 206
KEY_PLAY = 207
KEY_FASTFORWARD = 208
KEY_BASSBOOST = 209
KEY_PRINT = 210
KEY_HP = 211
KEY_CAMERA = 212
KEY_SOUND = 213
KEY_QUESTION = 214
KEY_EMAIL = 215
KEY_CHAT = 216
KEY_SEARCH = 217
KEY_CONNECT = 218
KEY_FINANCE = 219
KEY_SPORT = 220
KEY_SHOP = 221
KEY_ALTERASE = 222
KEY_CANCEL = 223
KEY_BRIGHTNESSDOWN = 224
KEY_BRIGHTNESSUP = 225
KEY_MEDIA = 226

KEY_UNKNOWN = 240

BTN_MISC = 0x100
BTN_0 = 0x100
BTN_1 = 0x101
BTN_2 = 0x102
BTN_3 = 0x103
BTN_4 = 0x104
BTN_5 = 0x105
BTN_6 = 0x106
BTN_7 = 0x107
BTN_8 = 0x108
BTN_9 = 0x109

BTN_MOUSE = 0x110
BTN_LEFT = 0x110
BTN_RIGHT = 0x111
BTN_MIDDLE = 0x112
BTN_SIDE = 0x113
BTN_EXTRA = 0x114
BTN_FORWARD = 0x115
BTN_BACK = 0x116
BTN_TASK = 0x117

BTN_JOYSTICK = 0x120
BTN_TRIGGER = 0x120
BTN_THUMB = 0x121
BTN_THUMB2 = 0x122
BTN_TOP = 0x123
BTN_TOP2 = 0x124
BTN_PINKIE = 0x125
BTN_BASE = 0x126
BTN_BASE2 = 0x127
BTN_BASE3 = 0x128
BTN_BASE4 = 0x129
BTN_BASE5 = 0x12a
BTN_BASE6 = 0x12b
BTN_DEAD = 0x12f

BTN_GAMEPAD = 0x130
BTN_A = 0x130
BTN_B = 0x131
BTN_C = 0x132
BTN_X = 0x133
BTN_Y = 0x134
BTN_Z = 0x135
BTN_TL = 0x136
BTN_TR = 0x137
BTN_TL2 = 0x138
BTN_TR2 = 0x139
BTN_SELECT = 0x13a
BTN_START = 0x13b
BTN_MODE = 0x13c
BTN_THUMBL = 0x13d
BTN_THUMBR = 0x13e

BTN_DIGI = 0x140
BTN_TOOL_PEN = 0x140
BTN_TOOL_RUBBER = 0x141
BTN_TOOL_BRUSH = 0x142
BTN_TOOL_PENCIL = 0x143
BTN_TOOL_AIRBRUSH = 0x144
BTN_TOOL_FINGER = 0x145
BTN_TOOL_MOUSE = 0x146
BTN_TOOL_LENS = 0x147
BTN_TOUCH = 0x14a
BTN_STYLUS = 0x14b
BTN_STYLUS2 = 0x14c
BTN_TOOL_DOUBLETAP = 0x14d
BTN_TOOL_TRIPLETAP = 0x14e

BTN_WHEEL = 0x150
BTN_GEAR_DOWN = 0x150
BTN_GEAR_UP = 0x151

KEY_OK = 0x160
KEY_SELECT = 0x161
KEY_GOTO = 0x162
KEY_CLEAR = 0x163
KEY_POWER2 = 0x164
KEY_OPTION = 0x165
KEY_INFO = 0x166
KEY_TIME = 0x167
KEY_VENDOR = 0x168
KEY_ARCHIVE = 0x169
KEY_PROGRAM = 0x16a
KEY_CHANNEL = 0x16b
KEY_FAVORITES = 0x16c
KEY_EPG = 0x16d
KEY_PVR = 0x16e
KEY_MHP = 0x16f
KEY_LANGUAGE = 0x170
KEY_TITLE = 0x171
KEY_SUBTITLE = 0x172
KEY_ANGLE = 0x173
KEY_ZOOM = 0x174
KEY_MODE = 0x175
KEY_KEYBOARD = 0x176
KEY_SCREEN = 0x177
KEY_PC = 0x178
KEY_TV = 0x179
KEY_TV2 = 0x17a
KEY_VCR = 0x17b
KEY_VCR2 = 0x17c
KEY_SAT = 0x17d
KEY_SAT2 = 0x17e
KEY_CD = 0x17f
KEY_TAPE = 0x180
KEY_RADIO = 0x181
KEY_TUNER = 0x182
KEY_PLAYER = 0x183
KEY_TEXT = 0x184
KEY_DVD = 0x185
KEY_AUX = 0x186
KEY_MP3 = 0x187
KEY_AUDIO = 0x188
KEY_VIDEO = 0x189
KEY_DIRECTORY = 0x18a
KEY_LIST = 0x18b
KEY_MEMO = 0x18c
KEY_CALENDAR = 0x18d
KEY_RED = 0x18e
KEY_GREEN = 0x18f
KEY_YELLOW = 0x190
KEY_BLUE = 0x191
KEY_CHANNELUP = 0x192
KEY_CHANNELDOWN = 0x193
KEY_FIRST = 0x194
KEY_LAST = 0x195
KEY_AB = 0x196
KEY_NEXT = 0x197
KEY_RESTART = 0x198
KEY_SLOW = 0x199
KEY_SHUFFLE = 0x19a
KEY_BREAK = 0x19b
KEY_PREVIOUS = 0x19c
KEY_DIGITS = 0x19d
KEY_TEEN = 0x19e
KEY_TWEN = 0x19f

KEY_DEL_EOL = 0x1c0
KEY_DEL_EOS = 0x1c1
KEY_INS_LINE = 0x1c2
KEY_DEL_LINE = 0x1c3

KEY_FN = 0x1d0
KEY_FN_ESC = 0x1d1
KEY_FN_F1 = 0x1d2
KEY_FN_F2 = 0x1d3
KEY_FN_F3 = 0x1d4
KEY_FN_F4 = 0x1d5
KEY_FN_F5 = 0x1d6
KEY_FN_F6 = 0x1d7
KEY_FN_F7 = 0x1d8
KEY_FN_F8 = 0x1d9
KEY_FN_F9 = 0x1da
KEY_FN_F10 = 0x1db
KEY_FN_F11 = 0x1dc
KEY_FN_F12 = 0x1dd
KEY_FN_1 = 0x1de
KEY_FN_2 = 0x1df
KEY_FN_D = 0x1e0
KEY_FN_E = 0x1e1
KEY_FN_F = 0x1e2
KEY_FN_S = 0x1e3
KEY_FN_B = 0x1e4

BTN_TRIGGER_HAPPY = 0x2c0           # These HAPPY constants are used
BTN_TRIGGER_HAPPY1 = 0x2c0          # by some recent joysticks for
BTN_TRIGGER_HAPPY2 = 0x2c1          # directional pads or buttons.
BTN_TRIGGER_HAPPY3 = 0x2c2
BTN_TRIGGER_HAPPY4 = 0x2c3
BTN_TRIGGER_HAPPY5 = 0x2c4
BTN_TRIGGER_HAPPY6 = 0x2c5
BTN_TRIGGER_HAPPY7 = 0x2c6
BTN_TRIGGER_HAPPY8 = 0x2c7
BTN_TRIGGER_HAPPY9 = 0x2c8
BTN_TRIGGER_HAPPY10 = 0x2c9
BTN_TRIGGER_HAPPY11 = 0x2ca
BTN_TRIGGER_HAPPY12 = 0x2cb
BTN_TRIGGER_HAPPY13 = 0x2cc
BTN_TRIGGER_HAPPY14 = 0x2cd
BTN_TRIGGER_HAPPY15 = 0x2ce
BTN_TRIGGER_HAPPY16 = 0x2cf
BTN_TRIGGER_HAPPY17 = 0x2d0
BTN_TRIGGER_HAPPY18 = 0x2d1
BTN_TRIGGER_HAPPY19 = 0x2d2
BTN_TRIGGER_HAPPY20 = 0x2d3
BTN_TRIGGER_HAPPY21 = 0x2d4
BTN_TRIGGER_HAPPY22 = 0x2d5
BTN_TRIGGER_HAPPY23 = 0x2d6
BTN_TRIGGER_HAPPY24 = 0x2d7
BTN_TRIGGER_HAPPY25 = 0x2d8
BTN_TRIGGER_HAPPY26 = 0x2d9
BTN_TRIGGER_HAPPY27 = 0x2da
BTN_TRIGGER_HAPPY28 = 0x2db
BTN_TRIGGER_HAPPY29 = 0x2dc
BTN_TRIGGER_HAPPY30 = 0x2dd
BTN_TRIGGER_HAPPY31 = 0x2de
BTN_TRIGGER_HAPPY32 = 0x2df
BTN_TRIGGER_HAPPY33 = 0x2e0
BTN_TRIGGER_HAPPY34 = 0x2e1
BTN_TRIGGER_HAPPY35 = 0x2e2
BTN_TRIGGER_HAPPY36 = 0x2e3
BTN_TRIGGER_HAPPY37 = 0x2e4
BTN_TRIGGER_HAPPY38 = 0x2e5
BTN_TRIGGER_HAPPY39 = 0x2e6
BTN_TRIGGER_HAPPY40 = 0x2e7

KEY_MAX = 0x2ff

# Relative axes

REL_X = 0x00
REL_Y = 0x01
REL_Z = 0x02
REL_RX = 0x03
REL_RY = 0x04
REL_RZ = 0x05
REL_HWHEEL = 0x06
REL_DIAL = 0x07
REL_WHEEL = 0x08
REL_MISC = 0x09
REL_MAX = 0x0f

# Absolute axes

ABS_X = 0x00
ABS_Y = 0x01
ABS_Z = 0x02
ABS_RX = 0x03
ABS_RY = 0x04
ABS_RZ = 0x05
ABS_THROTTLE = 0x06
ABS_RUDDER = 0x07
ABS_WHEEL = 0x08
ABS_GAS = 0x09
ABS_BRAKE = 0x0a
ABS_HAT0X = 0x10
ABS_HAT0Y = 0x11
ABS_HAT1X = 0x12
ABS_HAT1Y = 0x13
ABS_HAT2X = 0x14
ABS_HAT2Y = 0x15
ABS_HAT3X = 0x16
ABS_HAT3Y = 0x17
ABS_PRESSURE = 0x18
ABS_DISTANCE = 0x19
ABS_TILT_X = 0x1a
ABS_TILT_Y = 0x1b
ABS_TOOL_WIDTH = 0x1c
ABS_VOLUME = 0x20
ABS_MISC = 0x28
ABS_MAX = 0x3f

# Misc events

MSC_SERIAL = 0x00
MSC_PULSELED = 0x01
MSC_GESTURE = 0x02
MSC_RAW = 0x03
MSC_SCAN = 0x04
MSC_MAX = 0x07

# LEDs

LED_NUML = 0x00
LED_CAPSL = 0x01
LED_SCROLLL = 0x02
LED_COMPOSE = 0x03
LED_KANA = 0x04
LED_SLEEP = 0x05
LED_SUSPEND = 0x06
LED_MUTE = 0x07
LED_MISC = 0x08
LED_MAIL = 0x09
LED_CHARGING = 0x0a
LED_MAX = 0x0f

# Autorepeat values

REP_DELAY = 0x00
REP_PERIOD = 0x01
REP_MAX = 0x01

# Sounds

SND_CLICK = 0x00
SND_BELL = 0x01
SND_TONE = 0x02
SND_MAX = 0x07

# IDs.

ID_BUS = 0
ID_VENDOR = 1
ID_PRODUCT = 2
ID_VERSION = 3

BUS_PCI = 0x01
BUS_ISAPNP = 0x02
BUS_USB = 0x03
BUS_HIL = 0x04
BUS_BLUETOOTH = 0x05

BUS_ISA = 0x10
BUS_I8042 = 0x11
BUS_XTKBD = 0x12
BUS_RS232 = 0x13
BUS_GAMEPORT = 0x14
BUS_PARPORT = 0x15
BUS_AMIGA = 0x16
BUS_ADB = 0x17
BUS_I2C = 0x18
BUS_HOST = 0x19

# Values describing the status of an effect
FF_STATUS_STOPPED = 0x00
FF_STATUS_PLAYING = 0x01
FF_STATUS_MAX = 0x01

rel_raw_names = {}
abs_raw_names = {}
key_raw_names = {}
for _name, _val in locals().copy().items():
    if _name.startswith('REL_'):
        rel_raw_names[_val] = _name
    elif _name.startswith('ABS_'):
        abs_raw_names[_val] = _name
    elif _name.startswith('KEY_') or _name.startswith('BTN_'):
        key_raw_names[_val] = _name
