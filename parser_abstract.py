#!/bin/python

from tokenCode import TokenCode

class Parser():
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead = lexer.nextToken()

    def _pad(self, string):
        return ' ' + string + ' '

    def _match(self, tokenCode):
        if(tokenCode == self.lookahead.tokenCode):
            self.lookahead = self.lexer.nextToken()
        else:
            raise ValueError('Expected ' + tokenCode.name + ' in column: ' + str(self.lexer.currChar + 1))

    def _O(self):
        op = self.lookahead.lexeme
        self._match(TokenCode.Addop)
        return self._pad(op)

    def _T(self):
        num = self.lookahead.lexeme
        self._match(TokenCode.Number)
        return self._pad(num)

    def parse(self):
        e = self._E().strip()
        if self.lookahead.tokenCode != TokenCode.EOF:
            raise ValueError('Expected EOF in column: ' + str(self.lexer.currChar + 1))
        return e
