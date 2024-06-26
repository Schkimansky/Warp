from typing import Self
from constants import SYMBOLS, KEYWORDS


class Token:
    pass


class Int(Token):
    def __init__(self: Self, value: str) -> None:
        self.value: str = value

    def __str__(self): return f'Int("{self.value}")'


class Keyword(Token):
    def __init__(self: Self, value: str) -> None:
        self.value: str = value

    def __str__(self): return f'Keyword({self.value})'


class Identifier(Token):
    def __init__(self: Self, value: str) -> None:
        self.value: str = value

    def __str__(self): return f'Identifier("{self.value}")'


# Symbols
class Space(Token):
    def __init__(self: Self, value: str = SYMBOLS['Space']) -> None:
        self.value: str = value
        self.length = len(self.value)

    def __str__(self): return f'Space({self.length})'


class Equals(Token):
    def __init__(self: Self) -> None: pass
    def __str__(self): return f'Equals()'


class DoubleEquals(Token):
    def __init__(self: Self) -> None: pass
    def __str__(self): return f'DoubleEquals()'


class Plus(Token):
    def __init__(self: Self) -> None: pass
    def __str__(self): return f'Plus()'


class Minus(Token):
    def __init__(self: Self) -> None: pass
    def __str__(self): return f'Minus()'


class Multiply(Token):
    def __init__(self: Self) -> None: pass
    def __str__(self): return f'Multiply()'


class Divide(Token):
    def __init__(self: Self) -> None: pass
    def __str__(self): return f'Divide()'


# Wrap tokens
class LeftParenthesis(Token):
    def __init__(self: Self) -> None: pass
    def __str__(self): return f'LeftParenthesis()'


class RightParenthesis(Token):
    def __init__(self: Self) -> None: pass
    def __str__(self): return f'RightParenthesis()'


class Parenthesis(Token):
    def __init__(self: Self, inner_tokens: list[Token]) -> None: self.inner_tokens = inner_tokens
    def __str__(self): return f'Parenthesis({self.inner_tokens})'
