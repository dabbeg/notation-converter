#!/bin/python

from tokenCode import TokenCode

class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead = lexer.nextToken()

    def _match(self, tokenCode):
        if(tokenCode == self.lookahead.tokenCode):
            self.lookahead = self.lexer.nextToken()
        else:
            print('Expected ' + tokenCode.name)
            exit(1)

    def _O(self):
        op = self.lookahead.lexeme
        self._match(TokenCode.Addop)
        return op

    def _T(self):
        num = self.lookahead.lexeme
        self._match(TokenCode.Number)
        return num

    def parse(self):
        print(self._E())
