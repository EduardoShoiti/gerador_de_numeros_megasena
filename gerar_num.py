from random import randint

def gerar():
    global i
    global megasena
    i=0
    megasena = []
    while(i < 6):
        num = randint(1, 60)
        if num not in megasena:
            megasena.append(num)
            i += 1
    megasena.sort()
    return megasena