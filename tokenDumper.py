from lexer import Lexer
from tokenCode import TokenCode
import sys

if __name__ == "__main__":
    inp = sys.argv[1]
    lexer = Lexer(inp)

    token = lexer.nextToken()
    while token.tokenCode.name != TokenCode.EOF.name:
        print(token)
        token = lexer.nextToken()
