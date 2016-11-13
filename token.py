#!/bin/python

class Token:
    def __init__(self, tokenCode, lexeme, col):
        self.tokenCode = tokenCode
        self.lexeme = lexeme
        self.col = col

    def __str__(self):
        template = 'TokenCode: {0}, Lexeme: {1}, Column: {2}'
        return template.format(self.tokenCode.name, self.lexeme, str(self.col))


