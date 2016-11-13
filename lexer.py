#!/bin/python

import re
from tokenCode import TokenCode
from token import Token

#
# This is a lexical analyzer which is initialized
# with a expression and extracts tokens from it
#
class Lexer:
    def __init__(self, expr):
        self.expr = expr.replace(' ', '')
        self.currChar = 0

    #
    # Sync member variables after a token has been
    # extracted from the expression
    #
    def __sync__(self, lexeme):
        self.currChar += len(lexeme)
        self.expr = self.expr.replace(lexeme, '', 1)

    #
    # Get next token from the expression
    #
    def nextToken(self):
        if self.expr == "":
            return Token(TokenCode.EOF, "", self.currChar)

        # matches numbers
        m = re.compile('\d+').match(self.expr)
        if m != None:
            lexeme = m.group(0)
            token = Token(TokenCode.Number, lexeme, self.currChar)
            self.__sync__(lexeme)

            return token

        # matches addop
        m = re.compile('(\+|\-)').match(self.expr)
        if m != None:
            lexeme = m.group(0)
            token = Token(TokenCode.Addop, lexeme, self.currChar)
            self.__sync__(lexeme)

            return token

        # matches mulop
        m = re.compile('(\*|\/)').match(self.expr)
        if m != None:
            lexeme = m.group(0)
            token = Token(TokenCode.Mulop, lexeme, self.currChar)
            self.__sync__(lexeme)

            return token

        # matches unknown
        m = re.compile('.*?(?=(\+|\-|\d+))').match(self.expr)
        if m != None:
            lexeme = m.group(0)
            token = Token(TokenCode.Unknown, lexeme, self.currChar)
            self.__sync__(lexeme)

            return token

        raise Exception('Expression is not empty and was not matched to any token!')

