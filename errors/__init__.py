__all__ = ['Warning', 'Error', 
           'InternelError',
           'SyntaxError']

# 
# Base
# 

class Warning(Exception): pass
class Error(Exception):   pass

# 
# Error based
# 

class InternelError(Error): pass
class SyntaxError(Error): pass

_ = Warning, Error, InternelError, SyntaxError
