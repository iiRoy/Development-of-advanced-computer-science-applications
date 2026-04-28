import ply.lex as lex

keywords = {
    'while': 'WHILE',
    'if': 'IF'
}

tokens = [
    'INT',
    'ID',
    'LE',
    'PP'
] + list(keywords.values())

t_ignore = ' \t\n'

t_LE = r'<='
t_PP = r'\+\+'
literals = '+*/-(){},;='

def t_ID(t):
    r'[a-z][a-zA-Z0-9]*'
    if t.value in keywords:
        t.type = keywords[t.value]
    return t

def t_INT(t):
    r'[0-9](_?[0-9])*'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.skip(1)

lexer = lex.lex()

lexer.input("""
    int main() {
        int i = 0;
        while (a <= 5_5){
            i++;
        }
        return 1 + 1;
    }
""")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)