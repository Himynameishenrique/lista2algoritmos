"""
Q1.

Primeiro problema: para criar o atributo grau, deve-se localizar o primeiro
parâmetro maior que zero da esquerda pra direita.

Segundo problema: a derivada de um monômio de coeficiente C e grau N tem como coeficiente c*n e grau n-1. Por exemplo: 4x³ = 12x²

"""

class Polinomio:

    def __init__ (self,*cfx): #O operador "*" de Python permite múltiplos argumentos num só, na forma de tupla
        self.cfx=list(cfx) #O comando "list(argumento)" converte a tupla em uma lista
        while self.cfx[0]==0: #Deleta os argumentos não válidos
            self.cfx.pop[0]
        self.grau=len(self.cfx)-1
