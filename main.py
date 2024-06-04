import cProfile
from tokenizing.tokenizer import tokenize


# Found this to be the most optimal
workers = 2000
code_length = 15_000_000_0

data = 'e' * (code_length // workers)

cProfile.run('tokenize(data, workers)')
