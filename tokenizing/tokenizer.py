from constants import *
from tokenizing.tokens import *
from concurrent.futures import ThreadPoolExecutor
import errors


class Tokenizer:
    def __init__(self, text) -> None:
        self.text = list(text)
        self.tokens = []
        self.current_token = None

        for letter in self.text:
            self.check_character(letter)

        # Append last token to tokens
        self.on_new_different_token_type()

    # Checking functions
    def check_character(self, char) -> None:
        # Numbers
        fits_numbers = self.handle_numbers(char)
        if not fits_numbers:
            # Identifiers
            fits_identifiers = self.handle_identifiers(char)
            if not fits_identifiers:
                # Symbols
                fits_symbols = self.handle_symbols(char)
                if not fits_symbols:
                    fits_math_symbols = self.handle_math_symbols(char)
                    if not fits_math_symbols:
                        # Letter does not appear to fit with rules of the language
                        errors.SyntaxError('Invalid character:', char)

    # Handle functions, Used by check_character
    def handle_numbers(self, char) -> bool:
        # Previous character was int too, Add previous char with the new char
        if char in DIGITS and type(self.current_token) is not Identifier and type(self.current_token) is Int:
            self.current_token = Int(self.current_token.value + char)
            return True
        # Previous character was not an int, New token Int(x).
        elif char in DIGITS and type(self.current_token) is not Identifier and type(self.current_token) is not Int:
            # Append previous full token to tokens list. Only full strings are allowed in self.tokens
            self.on_new_different_token_type()
            self.current_token = Int(char)
            return True
        return False

    def handle_identifiers(self, char) -> bool:
        # Ascii, Previous tok was not an identifier
        if char in ASCII and type(self.current_token) is not Identifier:
            self.on_new_different_token_type()
            self.current_token = Identifier(char)
            return True
        # Ascii, Previous tok WAS an identifier (add previous and new one now)
        elif char in ASCII and type(self.current_token) is Identifier:
            self.current_token = Identifier(self.current_token.value + char)
            return True
        # Digits put on the end of identifier
        elif char in DIGITS and type(self.current_token) is Identifier:
            self.current_token = Identifier(self.current_token.value + char)
            return True
        return False

    def handle_symbols(self, char) -> bool:
        # Space
        # Space, Previous token was not an Space(), Therefore this is a new different token.
        if char in SYMBOLS['Space'] and type(self.current_token) is not Space:
            self.on_new_different_token_type()
            self.current_token = Space(SYMBOLS['Space'])
            return True

        # Space, Previous token WAS Space, So we should add the previous space to the new char.
        elif char in SYMBOLS['Space'] and type(self.current_token) is Space:
            self.current_token = Space(self.current_token.value + SYMBOLS['Space'])
            return True

        # Equals
        # Equals, Previous token was not an Equals(), Therefore this is a new different token.
        elif char in SYMBOLS['Equals'] and type(self.current_token) is not Equals:
            self.on_new_different_token_type()
            self.current_token = Equals()
            return True
        # Equals, Previous token WAS Equals(), Therefore this is a Double Equals instead.
        elif char in SYMBOLS['Equals'] and type(self.current_token) is Equals:
            self.on_new_different_token_type()
            self.current_token = DoubleEquals()
            return True
        return False

    def handle_math_symbols(self, char):
        # Math symbols (+ - * /)
        # Plus
        if char in SYMBOLS['Plus']:
            self.on_new_different_token_type()
            self.current_token = Equals()
            return True
        # Minus
        elif char in SYMBOLS['Minus']:
            self.on_new_different_token_type()
            self.current_token = Minus()
            return True
        # Multiply
        elif char in SYMBOLS['Multiply']:
            self.on_new_different_token_type()
            self.current_token = Multiply()
            return True
        # Divide
        elif char in SYMBOLS['Divide']:
            self.on_new_different_token_type()
            self.current_token = Divide()
            return True
        # LeftParenthesis
        elif char in SYMBOLS['LeftParenthesis']:
            self.on_new_different_token_type()
            self.current_token = LeftParenthesis()
            return True
        # RightParenthesis
        elif char in SYMBOLS['RightParenthesis']:
            self.on_new_different_token_type()
            self.current_token = RightParenthesis()
            return True
        return False

    # On_X functions
    def on_new_different_token_type(self):
        if self.current_token is not None:
            self.tokens.append(self.current_token)
        return


# Optimizes tokenizing
def tokenize(data: str, workers: int) -> list[Tokenizer]:
    chunk_size = len(data) // workers
    sections = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(lambda section: Tokenizer(section), section) for section in sections]

        return [future.result() for future in futures]

