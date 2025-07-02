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

# Inicio do programa
if umidade < 40:
    alerta("Monitor", " Ar seco detectado ")
