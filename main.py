import cProfile
from tokenizing.tokenizer import tokenize
<

# Found this to be the most optimal
workers = 35
code_length = 5000000


def profile():
    data = 'e' * (code_length // workers)
    return tokenize(data, workers)


cProfile.run('profile()')
