from ply.lex import lex
from ply.yacc import yacc
import sys
import os

# Lexer
reservados = {
    'dispositivo': 'DISPOSITIVO',
    'set': 'SET',
    'se': 'SE',
    'entao': 'ENTAO',
    'senao': 'SENAO',
    'enviar': 'ENVIAR',
    'alerta': 'ALERTA',
    'para': 'PARA',
    'todos': 'TODOS',
    'ligar': 'LIGAR',
    'desligar': 'DESLIGAR'
}

tokens = (
    'NUM',
    'ID',
    'STRING',
    'PONTO',
    'DOISPONTOS',
    'VIRGULA',
    'LBRACE',
    'RBRACE',
    'LPAR',
    'RPAR',
    'EQUALS',
    'OPLOGIC',
    'AND',
    'BOOL'
) + tuple(reservados.values())

t_PONTO = r'\.'
t_DOISPONTOS = r':'
t_VIRGULA = r','
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAR = r'\('
t_RPAR = r'\)'
t_EQUALS = r'='
t_OPLOGIC = r'==|!=|<=|>=|<|>'
t_AND = r'&&'
t_ignore = ' \t'

def t_COMMENT(t):
    r'//.*'
    pass

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value.upper() in ('TRUE', 'FALSE'):
        t.type = 'BOOL'
        t.value = (t.value.upper() == 'TRUE')
    else:
        t.type = reservados.get(t.value.lower(), 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Léxico: Caractere inválido na linha {t.lexer.lineno}: '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex()


# Parser
precedence = (('left', 'AND'),)

def p_program(p):
    'program : devices cmds'
    p[0] = ('program', p[1], p[2])

def p_devices_multiple(p):
    'devices : device devices'
    p[0] = [p[1]] + p[2]

def p_devices_single(p):
    'devices : device'
    p[0] = [p[1]]

def p_device(p):
    '''device : DISPOSITIVO DOISPONTOS LBRACE ID RBRACE
              | DISPOSITIVO DOISPONTOS LBRACE ID VIRGULA ID RBRACE'''
    if len(p) == 6:
        p[0] = ('device', p[4], None)
    else:
        p[0] = ('device', p[4], p[6])

def p_cmds_multiple(p):
    'cmds : command cmds'
    p[0] = [p[1]] + p[2]

def p_cmds_single(p):
    'cmds : command'
    p[0] = [p[1]]

def p_command(p):
    'command : cmd PONTO'
    p[0] = p[1]

def p_cmd(p):
    '''cmd : attrib
           | obsact
           | act'''
    p[0] = p[1]

def p_attrib(p):
    'attrib : SET ID EQUALS var'
    p[0] = ('set', p[2], p[4])

def p_var(p):
    '''var : NUM
           | BOOL'''
    p[0] = p[1]

def p_obsact_if(p):
    'obsact : SE obs ENTAO act'
    p[0] = ('if', p[2], p[4], None)

def p_obsact_if_else(p):
    'obsact : SE obs ENTAO act SENAO act'
    p[0] = ('if', p[2], p[4], p[6])

def p_obs_single(p):
    'obs : obs_base'
    p[0] = p[1]

def p_obs_and(p):
    'obs : obs_base AND obs'
    p[0] = ('and', p[1], p[3])

def p_obs_base(p):
    'obs_base : ID OPLOGIC var'
    p[0] = ('op', p[2], p[1], p[3])

def p_act_basic(p):
    'act : action ID'
    p[0] = (p[1][1], p[2])

def p_act_alert_msg(p):
    'act : ENVIAR ALERTA LPAR STRING RPAR ID'
    p[0] = ('alert_msg', p[6], p[4])

def p_act_alert_msg_sem_paren(p):
    'act : ENVIAR ALERTA STRING ID'
    p[0] = ('alert_msg', p[4], p[3])


def p_act_alert_msg_obs(p):
    'act : ENVIAR ALERTA LPAR STRING VIRGULA ID RPAR ID'
    p[0] = ('alert_msg_obs', p[8], p[4], p[6])

def p_act_alert_msg_obs_sem_paren(p):
    'act : ENVIAR ALERTA STRING VIRGULA ID ID'
    p[0] = ('alert_msg_obs', p[6], p[3], p[5])

def p_act_alert_msg_obs_all(p):
    '''act : ENVIAR ALERTA LPAR STRING VIRGULA ID RPAR PARA TODOS DOISPONTOS id_list'''
    p[0] = ('broadcast_obs', p[3], p[5], p[9])

def p_act_broadcast(p):
    'act : ENVIAR ALERTA LPAR STRING RPAR PARA TODOS DOISPONTOS id_list'
    p[0] = ('broadcast', p[4], p[9])


def p_action(p):
    '''action : LIGAR
              | DESLIGAR'''
    p[0] = ('action', p[1])

def p_id_list_multiple(p):
    'id_list : ID VIRGULA id_list'
    p[0] = [p[1]] + p[3]

def p_id_list_single(p):
    'id_list : ID'
    p[0] = [p[1]]

def p_error(p):
    if p:
        print(f"Sintaxe: Erro na linha {p.lineno}, token inesperado: {p.type} ('{p.value}')")
    else:
        print("Sintaxe: Erro no fim do arquivo, possivelmente faltando um '.'")

parser = yacc()

class CodeGenerator:
    def __init__(self):
        self.indent_level = 0
        self.observation_vars = set()
        self.initialized_vars = set()

    def _indent(self):
        return "    " * self.indent_level

    def generate(self, node):
        method_name = f'_generate_{node[0]}'
        method = getattr(self, method_name, self._generate_default)
        return method(node)

    def _generate_default(self, node):
        raise NotImplementedError(f"Nó sem gerador: {node[0]}")

    def _generate_program(self, node):
        _, devices, commands = node
        code = '''# Codigo gerado pelo compilador ObsAct -> Python

def ligar(namedevice):
    print(namedevice + " ligado!")

def desligar(namedevice):
    print(namedevice + " desligado!")

def alerta(namedevice, msg):
    print(namedevice + " recebeu o alerta :\\n")
    print(msg)

def alerta_obs(namedevice, msg, var):
    print(namedevice + " recebeu o alerta :\\n")
    print(msg + " " + str(var))
'''

        for device in devices:
            self.generate(device)

        for cmd in commands:
            if cmd[0] == 'set':
                self.initialized_vars.add(cmd[1])

        uninit = self.observation_vars - self.initialized_vars
        if uninit:
            code += "\n# Inicializacao automatica\n"
            for var in sorted(uninit):
                code += f"{var} = 0\n"

        code += "\n# Inicio do programa\n"
        for cmd in commands:
            code += self.generate(cmd) + "\n"

        return code

    def _generate_device(self, node):
        _, _, obs = node
        if obs:
            self.observation_vars.add(obs)
        return ""

    def _generate_set(self, node):
        _, var, value = node
        return f"{self._indent()}{var} = {value}"

    def _generate_if(self, node):
        _, cond, if_block, else_block = node
        code = f"{self._indent()}if {self.generate(cond)}:\n"
        self.indent_level += 1
        code += self.generate(if_block) + "\n"
        self.indent_level -= 1
        if else_block:
            code += f"{self._indent()}else:\n"
            self.indent_level += 1
            code += self.generate(else_block) + "\n"
            self.indent_level -= 1
        return code.strip()

    def _generate_op(self, node):
        _, op, left, right = node
        return f"{left} {op} {right}"

    def _generate_and(self, node):
        _, left, right = node
        return f"({self.generate(left)} and {self.generate(right)})"

    def _generate_ligar(self, node):
        _, dev = node
        return f'{self._indent()}ligar("{dev}")'

    def _generate_desligar(self, node):
        _, dev = node
        return f'{self._indent()}desligar("{dev}")'

    def _generate_alert_msg(self, node):
        _, dev, msg = node
        return f'{self._indent()}alerta("{dev}", {msg})'

    def _generate_alert_msg_obs(self, node):
        _, dev, msg, var = node
        return f'{self._indent()}alerta_obs("{dev}", {msg}, {var})'

    def _generate_broadcast(self, node):
        _, msg, devices = node
        code = f"{self._indent()}# Broadcast para todos\n"
        for dev in devices:
            code += f'{self._indent()}alerta("{dev}", {msg})\n'
        return code.strip()

    def _generate_broadcast_obs(self, node):
        _, msg, var, devices = node
        code = f"{self._indent()}# Broadcast para todos com variável\n"
        for dev in devices:
            code += f'{self._indent()}alerta_obs("{dev}", {msg}, {var})\n'
        return code.strip()



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python compilador.py <arquivo.obsact>")
        sys.exit(1)

    entrada = sys.argv[1]
    if not entrada.endswith('.obsact'):
        print("Erro: A entrada deve ter extensão '.obsact'")
        sys.exit(1)

    try:
        with open(entrada, 'r') as f:
            codigo = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{entrada}' não encontrado.")
        sys.exit(1)

    ast = parser.parse(codigo, lexer=lexer)

    if ast:
        generator = CodeGenerator()
        saida = generator.generate(ast)
        nome_saida = os.path.splitext(entrada)[0] + '.py'
        with open(nome_saida, 'w') as f:
            f.write(saida)
        print(f"Compilação bem-sucedida. Arquivo gerado: {nome_saida}")
    else:
        print("Erro de sintaxe. Código não gerado.")
