import ply.lex as lex
import ply.yacc as yacc

from visitors import Calculator, Literal, BinaryOp

"""
  Program         ⇒  int  main ( ) { Declarations Statements }
  Declarations    ⇒  { Declaration }
  Declaration     ⇒  Type  Identifier  ;
  Type            ⇒  int | bool | float | char
  Statements      ⇒  { Statement }
  Statement       ⇒  ; | Block | Assignment | IfStatement | WhileStatement
  Block           ⇒  { Statements }
  Assignment      ⇒  Identifier = Expression ;
  IfStatement     ⇒  if ( Expression ) Statement [ else Statement ]

  WhileStatement  ⇒  while ( Expression ) Statement  
  Expression      ⇒  Conjunction { || Conjunction }
  Conjunction     ⇒  Equality { && Equality }

  Equality        ⇒  Relation [ EquOp Relation ]
  EquOp           ⇒  == | != 
  Relation        ⇒  Addition [ RelOp Addition ]

  RelOp           ⇒  < | <= | > | >= 

  Addition        ⇒  Term { AddOp Term }
  AddOp           ⇒  + | -
  Term            ⇒  Factor { MulOp Factor }
  MulOp           ⇒  * | / | %
  Factor          ⇒  [ UnaryOp ] Primary
  UnaryOp         ⇒  - | !
  Primary         ⇒  Identifier | IntLit | FloatLit |  ( Expression )
"""

reserved_words = {
    'int': 'INT',
    'while': 'WHILE',
    'return': 'RETURN'
}

tokens = [
    'ID',
    'INTLIT',
    'FLOATLIT',
    'LE',
    'GE',
    'EQ',
    'NEQ',
    'STR'
]+ list(reserved_words.values())

t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NEQ = r'!='

literals = '+*/-(){},;='

def t_ID(t):
    r'[a-z][a-zA-Z0-9]*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t

def t_FLOATLIT(t):
    r"\d(_?\d)*.\d(_?\d)*"
    t.value = float(t.value)
    return t

def t_INTLIT(t):
    r"\d(_?\d)*"
    t.value = int(t.value)
    return t

t_ignore=" \t\n"

lexer = lex.lex()

lexer.input("3.15 * r * r")

while True:
    t = lexer.token()
    print(t)
    if t == None:
        break

def p_Relation(p):
    """
    Relation : Relation RelOp Addition
        | Addition
    """

def p_RelOp(p):
    """
    RelOp : '<' 
        | LE 
        | '>' 
        | GE
    """

def p_Addition(p):
    """
    Addition : Addition AddOp Term
        | Term
    """

def p_AddOp(p):
    """
    AddOp : '+' 
        | '-'
    """

def p_Term(p):
    """
    Term : Term MulOp Factor
        | Factor
    """

def p_Primary(p):
    """
    Primary : ID 
        | INTLIT 
        | FLOATLIT 
        | '(' Addition ')'
    """

def p_UnaryOp(p):
    """
    UnaryOp : '-'
        | '!'
    """

def p_MulOp(p):
    """
    MulOp : '*' 
        | '/' 
        | '%'
    """

def p_Factor(p):
    """
    Factor : UnaryOp Primary
        | Primary
    """

program = """
(3.1415 * r * r) >= 50.0
"""

parser = yacc.yacc()

print(parser.parse(program))