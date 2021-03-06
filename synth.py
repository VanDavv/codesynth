import os

import pysynth as ps
import uuid

mapping = {
    1: 'a0',
    2: 'a#0',
    3: 'b0',
    4: 'c1',
    5: 'c#1',
    6: 'd1',
    7: 'd#1',
    8: 'e1',
    9: 'f1',
    10: 'f#1',
    11: 'g1',
    12: 'g#1',
    13: 'a1',
    14: 'a#1',
    15: 'b1',
    16: 'c2',
    17: 'c#2',
    18: 'd2',
    19: 'd#2',
    20: 'e2',
    21: 'f2',
    22: 'f#2',
    23: 'g2',
    24: 'g#2',
    25: 'a2',
    26: 'a#2',
    27: 'b2',
    28: 'c3',
    29: 'c#3',
    30: 'd3',
    31: 'd#3',
    32: 'e3',
    33: 'f3',
    34: 'f#3',
    35: 'g3',
    36: 'g#3',
    37: 'a3',
    38: 'a#3',
    39: 'b3',
    40: 'c4',
    41: 'c#4',
    42: 'd4',
    43: 'd#4',
    44: 'e4',
    45: 'f4',
    46: 'f#4',
    47: 'g4',
    48: 'g#4',
    49: 'a4',
    50: 'a#4',
    51: 'b4',
    52: 'c5',
    53: 'c#5',
    54: 'd5',
    55: 'd#5',
    56: 'e5',
    57: 'f5',
    58: 'f#5',
    59: 'g5',
    60: 'g#5',
    61: 'a5',
    62: 'a#5',
    63: 'b5',
    64: 'c6',
    65: 'c#6',
    66: 'd6',
    67: 'd#6',
    68: 'e6',
    69: 'f6',
    70: 'f#6',
    71: 'g6',
    72: 'g#6',
    73: 'a6',
    74: 'a#6',
    75: 'b6',
    76: 'c7',
    77: 'c#7',
    78: 'd7',
    79: 'd#7',
    80: 'e7',
    81: 'f7',
    82: 'f#7',
    83: 'g7',
    84: 'g#7',
    85: 'a7',
    86: 'a#7',
    87: 'b7',
    88: 'c8',
}


def encode(char):
    index = ((ord(char) + 10) % 88) + 1
    return mapping[index], 16


def synthesize(text):
    notes = list(map(encode, text))
    if not os.path.exists('output'):
        os.makedirs('output')
    filename = os.path.join('output', uuid.uuid4().hex + '.wav')
    ps.make_wav(notes, fn=filename)
    return filename


if __name__ == '__main__':
    with open('samplescript.py', 'r') as file:
        synthesize(file.read())
