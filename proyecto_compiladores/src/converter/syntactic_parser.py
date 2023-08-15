from .converter import Converter
from ..ply import yacc

class SyntacticParser(object):

    # Tokens
    tokens = (
        "NUMBER",
        "DESTINY"
    )

    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.converter = Converter()

    #
    def p_instruction_conversion(self, p):
        'instruction : NUMBER DESTINY'
        p[0] = self.converter.convert(int(p[1]), p[2])

    # Regla de manejo de errores de sintaxis
    def p_error(self, p):
        print("Caracter no válido")

    # Ejecuta el analizador léxico
    def parse(self, input_string):
        return self.parser.parse(input_string)
