#!/bin/python

from tokenCode import TokenCode
from parser_abstract import Parser

class Parser(Parser):
    def _E(self):
        t = self._T()
        e_marked = self._E_marked()
        return e_marked['op'] + t + e_marked['val']

    def _E_marked(self):
        if self.lookahead.tokenCode == TokenCode.Number:
            t = self._T()
            o = self._O()
            e_marked = self._E_marked()
            return { 'val': t + e_marked['val'], 'op': e_marked['op'] + o }
        else:
            return { 'val': '', 'op': '' }
