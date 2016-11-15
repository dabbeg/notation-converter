#!/bin/python

from tokenCode import TokenCode
from parser_abstract import Parser

class Parser(Parser):
    def _E(self):
        t = self._T()
        e_marked = self._E_marked()
        return e_marked['op'] + t + e_marked['val']

    def _E_marked(self):
        if self.lookahead.tokenCode == TokenCode.Addop or self.lookahead.tokenCode == TokenCode.Mulop:
            o = self._O()
            t = self._T()
            e_marked = self._E_marked()
            return { 'val': e_marked['val'] + t, 'op': e_marked['op'] + o }
        else:
            return { 'val': '', 'op': '' }
