from lexer import Lexer
from tokenCode import TokenCode
import parser_prefix_to_infix
import parser_prefix_to_postfix
import parser_infix_to_prefix
import parser_infix_to_postfix
import parser_postfix_to_prefix
import parser_postfix_to_infix
import sys

def run(conversion, input):
    lexer = Lexer(input)

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
        raise ValueError('no parser of type: ' + conversion)

    return parser.parse()


if __name__ == "__main__":
    parsed_input = run(sys.argv[1], sys.argv[2])
    print(parsed_input)
