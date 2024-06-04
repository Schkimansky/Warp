from tokenizing.tokenizer import tokenize_fast, tokenize

code = \
"""me_using + amazing_module
"""

tokens = tokenize(code)
print(f'Code:\n{code}\n-----------')
print(*tokens)
