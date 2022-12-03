from plover.system.english_stenotype import *

KEYS = (
  '#', '^-', '+-',
  'S-', 'T-', 'K-', 'P-', 'W-', 'H-', 'R-',
  'A-', 'O-',
  '@', '*',
  '-E', '-U',
  '-F', '-R', '-P', '-B', '-L', '-G', '-T', '-S', '-D', '-Z',
)

IMPLICIT_HYPHEN_KEYS = ('A-', 'O-', '-E', '-U', '@', '*')

NUMBERS = {
    'S-': '1-',
    'T-': '2-',
    'P-': '3-',
    'H-': '4-',
    'A-': '5-',
    'O-': '6-',
    '-F': '-7',
    '-P': '-8',
    '-L': '-9',
    '-S': '-0'
}

KEYMAPS = {
    'Keyboard': {
        '#'         : ('q', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        '^-'        : 'Tab',
        '+-'        : '1', ## just used to suppress the warning
        'S-'        : 'a',
        'T-'        : 'w',
        'K-'        : 's',
        'P-'        : 'e',
        'W-'        : 'd',
        'H-'        : 'r',
        'R-'        : 'f',
        'A-'        : 'c',
        'O-'        : 'v',
        '*'         : ('y', 'h'),
        '@'         : ('t', 'g'),
        '-E'        : 'n',
        '-U'        : 'm',
        '-F'        : 'u',
        '-R'        : 'j',
        '-P'        : 'i',
        '-B'        : 'k',
        '-L'        : 'o',
        '-G'        : 'l',
        '-T'        : 'p',
        '-S'        : ';',
        '-D'        : '[',
        '-Z'        : '\'',
        'arpeggiate': 'space',
        # Suppress adjacent keys to prevent miss-strokes.
        'no-op'     : ('z', 'x', 'b', ',', '.', '/', ']', '\\'),
    },
}
