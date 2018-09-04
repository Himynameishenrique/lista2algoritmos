"""
Q1.

Segundo problema: a derivada de um monômio de coeficiente C e grau N tem como coeficiente c*n e grau n-1.
Por exemplo: 4x³ = 12x²

"""
import numpy as np

class Polinomio:

    def __init__ (self,*cfx): #O operador "*" de Python permite múltiplos argumentos num só, na forma de tupla
        self.cfx=list(cfx) #O comando "list(argumento)" converte a tupla em uma lista
        while self.cfx[0]==0: #Deleta os argumentos não válidos
            self.cfx.pop[0]
        self.grau=len(self.cfx)-1 #Armazena o grau


"""
Q2.
Primeiro problema: 
"""

class Matriz:
    def __init__ (self,linhas,colunas):
            self.__vetorApoio=np.eye(linhas,colunas) #Como não foi especificado o conteudo da matriz, optei pela identidade

    def __getitem__(self,*argumentos):
        argumentos=list(argumentos)
        if len(argumentos)>2 or len(argumentos)<1:
            raise ValueError ("Argumentos inválidos")
        elif len(argumentos)==2:
            linha=argumentos[0]
            coluna=argumentos
            [1]
            return self.__vetorApoio[linha,coluna]
        else:
            return self.__vetorApoio[argumentos]
        
        

