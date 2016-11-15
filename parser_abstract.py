#!/bin/python

from tokenCode import TokenCode

class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead = lexer.nextToken()

    def _match(self):
        self.lookahead = self.lexer.nextToken()

    def _O(self):
        op = self.lookahead.lexeme
        self._match()
        return op

    def _T(self):
        num = self.lookahead.lexeme
        self._match()
        return num

    def parse(self):
        print(self._E())
