# compilador.py

from ply.lex import lex
from ply.yacc import yacc
import sys

# Léxico
reservados = {
    'dispositivo': 'DISPOSITIVO',
    'set':         'SET',
    'se':          'SE',
    'entao':       'ENTAO',
    'senao':       'SENAO',
    'enviar':      'ENVIAR',
    'alerta':      'ALERTA',
    'para':        'PARA',
    'todos':       'TODOS',
    'ligar':       'LIGAR',
    'desligar':    'DESLIGAR',
}

tokens = (
    # Literais
    'NUM',        # números (VAR pode abranger boleano ou VAR)
    'ID',
    'PONTO',
    'DOISPONTOS',
    'VIRGULA',
    'LBRACE',
    'RBRACE',
    'LPAR',
    'RPAR',
    'OPLOGIC',    # == != < > <= >=
    'AND',        # &&
) + tuple(reservados.values())

# Expressões regulares para pontuação e operadores
t_PONTO       = r'\.'
t_DOISPONTOS  = r':'
t_VIRGULA     = r','
t_LBRACE      = r'\{'
t_RBRACE      = r'\}'
t_LPAR        = r'\('
t_RPAR        = r'\)'
t_OPLOGIC     = r'(==|!=|<=|>=|<|>)'
t_AND         = r'&&'

# Ignorar espaços e comentários de linha
t_ignore      = ' \t'
def t_COMMENT(t):
    r'//.*'
    pass

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Identificadores (namedevice, observation, msg)
def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reservados.get(t.value.lower(), 'ID')
    return t

# Erro léxico
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex()

# Sintático
def p_namedevice_list_single(p):
    'namedevice_list : ID'
    p[0] = [p[1]]

def p_namedevice_list_multi(p):
    'namedevice_list : ID VIRGULA namedevice_list'
    p[0] = [p[1]] + p[3]

# DEVICE -> dispositivo : { namedevice_list }
def p_device(p):
    'device : DISPOSITIVO DOISPONTOS LBRACE namedevice_list RBRACE'
    p[0] = p[4]

# DEVICES -> device devices | device
def p_devices_recursive(p):
    'devices : device devices'
    p[0] = p[1] + p[2]

def p_devices_single(p):
    'devices : device'
    p[0] = p[1]

# Atribuição: set observation = ID
# (VAR pode ser NUM ou ID para booleano)
def p_atribuicao(p):
    'atribuicao : SET ID OPLOGIC ID'
    p[0] = ('set', p[2], p[3], p[4])

# Condicional sem else: se observation oplogic ID entao cmds
def p_condicional(p):
    'condicional : SE ID OPLOGIC ID ENTAO cmds'
    p[0] = ('if', p[2], p[3], p[4], p[6], None)

# Condicional com else: se observation oplogic ID entao cmds senao cmds
def p_condicional_senao(p):
    'condicional : SE ID OPLOGIC ID ENTAO cmds SENAO cmds'
    p[0] = ('if', p[2], p[3], p[4], p[6], p[8])

# Ação simples: ligar|desligar namedevice
def p_acao(p):
    'acao : LIGAR ID'
    p[0] = ('action', 'ligar', p[2])

def p_acao_desligar(p):
    'acao : DESLIGAR ID'
    p[0] = ('action', 'desligar', p[2])

# Enviar alerta: enviar alerta ( ID ) ID
def p_enviar_alerta(p):
    'obsact : ENVIAR ALERTA LPAR ID RPAR ID'
    p[0] = ('alert', p[4], p[6])

# Broadcast: enviar alerta ( ID ) para todos : namedevice_list
def p_broadcast(p):
    'obsact : ENVIAR ALERTA LPAR ID RPAR PARA TODOS DOISPONTOS namedevice_list'
    p[0] = ('broadcast', p[4], p[10])

# Sequência de comandos: cmds -> (atribuicao|condicional|obsact|acao) cmds | único
def p_cmds_recursive(p):
    '''cmds : atribuicao cmds
             | condicional cmds
             | obsact cmds
             | acao cmds'''
    p[0] = [p[1]] + p[2]

def p_cmds_single(p):
    '''cmds : atribuicao
             | condicional
             | obsact
             | acao'''
    p[0] = [p[1]]

# Programa completo: devices cmds PONTO
def p_programa(p):
    'programa : devices cmds PONTO'
    p[0] = {'devices': p[1], 'commands': p[2]}

# Tratamento de erro sintático
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: {p.value}")
    else:
        print("Erro de sintaxe: fim de entrada inesperado")

tstart = 'programa'
parser = yacc()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python compilador.py <arquivo.obs>")
        sys.exit(1)

    arquivo_in = sys.argv[1]
    try:
        with open(arquivo_in, 'r') as f:
            texto = f.read()
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {arquivo_in}")
        sys.exit(1)

    result = parser.parse(texto)
    print(result)
