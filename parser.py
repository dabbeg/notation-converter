from lexer import Lexer
from tokenCode import TokenCode
import parser_prefix_to_infix
import parser_prefix_to_postfix
import parser_infix_to_prefix
import parser_infix_to_postfix
import parser_postfix_to_prefix
import parser_postfix_to_infix
import sys

if __name__ == "__main__":
    inp = sys.argv[2]
    lexer = Lexer(inp)

    conversion = sys.argv[1]

    if conversion == 'prefix-infix':
        parser = parser_prefix_to_infix.Parser(lexer)
    elif conversion == 'prefix-postfix':
        parser = parser_prefix_to_postfix.Parser(lexer)
    elif conversion == 'infix-prefix':
        parser = parser_infix_to_prefix.Parser(lexer)
    elif conversion == 'infix-postfix':
        parser = parser_infix_to_postfix.Parser(lexer)
    elif conversion == 'postfix-prefix':
        parser = parser_postfix_to_prefix.Parser(lexer)
    elif conversion == 'postfix-infix':
        parser = parser_postfix_to_infix.Parser(lexer)
    else:
        print('no parser of that type')
        exit(1)

    parser.parse()
