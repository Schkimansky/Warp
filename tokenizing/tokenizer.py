from constants import *
from tokenizing.tokens import *
import errors
from concurrent.futures import ThreadPoolExecutor


class Tokenizer:
    def __init__(self, text) -> None:
        self.text = list(text)
        # -1 because it will read at 0 instead of 1 when self.next_shar() is called for the first time
        self.index = -1
        self.tokens = []
        self.current_token = None

        for _ in self.text:
            self.next_char()

        self.on_end_token()

    # Checking functions
    def check_character(self, char) -> None:
        # Numbers
        # Previous character was int too, Add previous char with the new char
        if char in DIGITS and type(self.current_token) is not Identifier and type(self.current_token) is Int:
            self.current_token = Int(self.current_token.value + char)
        # Previous character was not an int, New token Int(x) in the makings!
        elif char in DIGITS and type(self.current_token) is not Identifier and type(self.current_token) is not Int:
            # Append previous full token to tokens list. Only full strings are allowed in self.tokens
            self.on_new_different_token_type()
            self.current_token = Int(char)

        # Identifiers
        # Ascii, Previous tok was not an identifier
        elif char in ASCII and type(self.current_token) is not Identifier:
            self.on_new_different_token_type()
            self.current_token = Identifier(char)
        # Ascii, Previous tok WAS an identifier (add previous and new one now)
        elif char in ASCII and type(self.current_token) is Identifier:
            self.current_token = Identifier(self.current_token.value + char)
        # Digits put on the end of identifier
        elif char in DIGITS and type(self.current_token) is Identifier:
            self.current_token = Identifier(self.current_token.value + char)

        # Some characters like = and ?.
        # Space
        # Space, Previous token was not an Space(), Therefore this is a new different token.
        elif char in SYMBOLS['Space'] and type(self.current_token) is not Space:
            self.on_new_different_token_type()
            self.current_token = Space(SYMBOLS['Space'])
        # Space, Previous token WAS Space, So we should add the previous space to the new char.
        elif char in SYMBOLS['Space'] and type(self.current_token) is Space:
            self.current_token = Space(self.current_token.value + SYMBOLS['Space'])

        # Equals
        # Equals, Previous token was not an Equals(), Therefore this is a new different token.
        elif char in SYMBOLS['Equals'] and type(self.current_token) is not Equals:
            self.on_new_different_token_type()
            self.current_token = Equals()
        # Equals, Previous token WAS Equals(), Therefore this is a Double Equals instead.
        elif char in SYMBOLS['Equals'] and type(self.current_token) is Equals:
            self.on_new_different_token_type()
            self.current_token = DoubleEquals()

        # Math symbols (+ - * /)
        # Plus
        elif char in SYMBOLS['Plus']:
            self.on_new_different_token_type()
            self.current_token = Equals()
        # Minus
        elif char in SYMBOLS['Minus']:
            self.on_new_different_token_type()
            self.current_token = Minus()
        # Multiply
        elif char in SYMBOLS['Multiply']:
            self.on_new_different_token_type()
            self.current_token = Multiply()
        # Divide
        elif char in SYMBOLS['Divide']:
            self.on_new_different_token_type()
            self.current_token = Divide()
        # LeftParenthesis
        elif char in SYMBOLS['LeftParenthesis']:
            self.on_new_different_token_type()
            self.current_token = LeftParenthesis()
        # RightParenthesis
        elif char in SYMBOLS['RightParenthesis']:
            self.on_new_different_token_type()
            self.current_token = RightParenthesis()

        # Letter does not appear to fit with rules of the language,
        else:
            errors.SyntaxError('Invalid character:', char)

    # Next functions
    def next_char(self):
        self.index += 1

        # No need to check for IndexOutOfBounds error,
        # Cuz we are running this function "next_char" exactly times the length of code
        char = self.text[self.index]

        self.check_character(char)

    # On_X functions
    def on_end_token(self):
        self.tokens.append(self.current_token)
        return

    def on_new_different_token_type(self):
        if self.current_token is not None:
            self.tokens.append(self.current_token)
        return


def tokenize(data: str, workers: int) -> list[Tokenizer]:
    chunk_size = len(data) // workers
    sections = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(lambda section: Tokenizer(section), section) for section in sections]

        return [future.result() for future in futures]

