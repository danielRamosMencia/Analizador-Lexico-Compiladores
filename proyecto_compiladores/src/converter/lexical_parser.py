from ..ply import lex

class LexicalParser(object):
    # Tokens
    tokens = (
        "NUMBER",
        "DESTINY"
    )

    # Patrones de tokens
    t_DESTINY   = r"hexadecimal|octal|binary|roman|alternative|random"

    # Ignora espacios y tabulaciones
    t_ignore  = " \t"

    # Ignora comentarios
    t_ignore_COMMENT = r"\#.*"

    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Regla para rastrear los números
    def t_NUMBER(self, t):
        r"\d+"
        t.value = int(t.value)    
        return t

    # Regla para rastrear los números de línea
    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    # Regla de manejo de errores
    def t_error(self, t):
        print(f"Caracter no válido '{t.value[0]}'")
        t.lexer.skip(1)
    
    # Ejecuta el analizador léxico
    def parse(self, data):
        result = []
        
        self.lexer.input(data)

        for tok in self.lexer:
            result.append(tok)
        return result
