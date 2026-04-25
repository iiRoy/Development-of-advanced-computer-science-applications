import ply.lex as lex

# Palabras reservadas de C
reserved_words = {
    'int':    'INT',
    'float':  'FLOAT',
    'char':   'CHAR',
    'void':   'VOID',
    'if':     'IF',
    'else':   'ELSE',
    'while':  'WHILE',
    'for':    'FOR',
    'return': 'RETURN',
}

tokens = [
    'ID',     # identificadores: variables y funciones
    'LINT',   # literales enteros: 42
    'LFLOAT', # literales flotantes: 3.14
    'LCHAR',  # literales de carácter: 'a'
    'STR',    # literales de cadena: "pato"
    'LE',     # <=
    'GE',     # >=
    'EQ',     # ==
    'NEQ',    # !=
    'INC',    # ++
    'DEC',    # --
] + list(reserved_words.values())

# Operadores de dos caracteres
t_LE  = r'<='
t_GE  = r'>='
t_EQ  = r'=='
t_NEQ = r'!='
t_INC = r'\+\+'
t_DEC = r'--'

# Caracteres simples 
literals = '+-*/=<>!,;(){}[]'

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved_words.get(t.value, 'ID')
    return t

def t_LFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_LINT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_LCHAR(t):
    r"'([^'\\]|\\.)*'"
    t.value = t.value[1:-1]  
    return t

def t_STR(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  
    return t

def t_COMMENT(t):
    r'//[^\n]*'
    pass  

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Código C

codigo_c = """
int factorial(int n) {
    int resultado;
    resultado = 1;
    for (int i = 1; i <= n; i++) {
        resultado = resultado * i;
    }
    return resultado;
}

float promedio(int a, int b) {
    return (a + b) / 2.0;
}

int main() {
    int n;
    float prom;
    char inicial;

    n = 5;
    prom = promedio(n, 10);
    inicial = 'A';

    if (prom >= 7.5) {
        n++;
    } else {
        n--;
    }

    while (n != 0) {
        n--;
    }

    return 0;
}
"""

lexer.input(codigo_c)
for tok in lexer:
    print(tok)

# Por qué estos tokens y no otros 
#
# TOKENS INCLUIDOS:
#   INT, FLOAT, CHAR, VOID
#       Los cuatro tipos de datos más usados en C real.
#
#   IF, ELSE, WHILE, FOR, RETURN
#       Estructuras de control fundamentales. 
#
#   ID, LINT, LFLOAT, LCHAR, STR
#       Cubre los cuatro tipos de literales más comunes.
#
#   LE, GE, EQ, NEQ  (<=, >=, ==, !=)
#       Los cuatro operadores relacionales de dos caracteres.
#
#   INC, DEC  (++, --)
#       Muy comunes en loops for y while. 
#
# TOKENS DEJADOS FUERA (y por qué):
#
#   &&, ||
#       Operadores lógicos. Comunes pero añaden complejidad
#       al parser. 
#
#   struct, typedef, switch, case, break, continue
#       Construcciones más avanzadas. 
#
#   ->, *  como puntero
#       El manejo de punteros requiere contexto del parser
#       para distinguir * multiplicación de * desreferencia.
#       Se omite para mantener el lexer simple.
#
#   Comentarios /* ... */
#       Requieren manejar saltos de línea explícitamente.
