# No emojis for this language, Do not enable.
# import emoji
# EMOJIS = [e for e in emoji.EMOJI_DATA.keys()]

DIGITS = list('0123456789')
ASCII = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()) + DIGITS + ['_', '?']

KEYWORDS = {}
SYMBOLS = {'Dot':      '.',
           'Space':    ' ',
           'Question': '?',
           'Equals':   '=',
           # Maths
           'Plus':     '+',
           'Minus':    '-',
           'Multiply': '*',
           'Divide':   '/',
           # Common
           'LeftParenthesis': '(',
           'RightParenthesis': ')',
           }
