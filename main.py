from tokenizing.tokenizer import tokenize_fast, tokenize

code = \
"""import amazing_module
"""

tokens = tokenize(code)
print(f'Code:\n{code}\n-----------')
print(*tokens)
