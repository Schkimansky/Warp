from tokenizing.tokenizer import tokenize_fast, tokenize

code = """e()"""

tokens = tokenize(code)
print(f'Code:\n{code}\n-----------')
print(*tokens)
