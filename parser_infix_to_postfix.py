#!/bin/python

from tokenCode import TokenCode
from parser_abstract import Parser

class Parser(Parser):
    def _E(self):
        t = self._T()
        e_marked = self._E_marked()
        return t + e_marked

    def _E_marked(self):
        if self.lookahead.tokenCode == TokenCode.Addop or self.lookahead.tokenCode == TokenCode.Mulop:
            o = self._O()
            t = self._T()
            e_marked = self._E_marked()
            return t + o + e_marked
        else:
            return ''
