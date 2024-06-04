from tokenizing.tokenizer import tokenize_fast, tokenize

code = \
"""

e

"""

print('start')
tokens = tokenize(code)
print(*tokens)
