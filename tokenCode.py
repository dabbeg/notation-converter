#!/bin/python

from enum import Enum

class TokenCode(Enum):
    Number = 1
    Addop = 2
    Mulop = 3
    Unknown = 4
    EOF = 5
