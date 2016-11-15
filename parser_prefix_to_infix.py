#!/bin/python

from tokenCode import TokenCode
from parser_abstract import Parser

class Parser(Parser):
    def _E(self):
        if self.lookahead.tokenCode == TokenCode.Number:
            return self._T()
        else:
            o = self._O()
            e = self._E()
            t = self._T()
            return e + o + t
