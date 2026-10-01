from animepython.lexer import tokenize_source

source = """\
season Character:
    episode greet(self):
        announce("Hello!")
"""

for token in tokenize_source(source):
    print(token)