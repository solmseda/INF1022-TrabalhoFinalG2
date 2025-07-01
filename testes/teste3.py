# Codigo gerado pelo compilador ObsAct -> Python

def ligar(namedevice):
    print(namedevice + " ligado!")

def desligar(namedevice):
    print(namedevice + " desligado!")

def alerta(namedevice, msg):
    print(namedevice + " recebeu o alerta :\n")
    print(msg)

def alerta_obs(namedevice, msg, var):
    print(namedevice + " recebeu o alerta :\n")
    print(msg + " " + str(var))

# Inicializacao automatica
movimento = 0
umidade = 0

# Inicio do programa
potencia = 100
if umidade < 40:
    alerta("Monitor", "Ar seco detectado")
if movimento == True:
    ligar("lampada")
else:
    desligar("lampada")
