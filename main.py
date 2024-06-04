from tokenizing.tokenizer import tokenize

code = 'e' * 1_000_000

print('start')
tokens = tokenize(code)
print(*tokens)
