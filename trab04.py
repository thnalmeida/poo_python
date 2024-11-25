#TRABALHO 04 - POO 2024/2

#trabalho com classe e metodos abstratos. isto eh, a classe terreno nao pode ser instanciada diretamente, pois qlq terreno
#tem seu proprio formato e, por isso, cada um tem o calculo de area e de peso à sua maneira (classe abstrata)
from abc import ABC, abstractmethod

#criando superclasse terreno
class Terreno:
    def __init__(self, nome: str, localizacao: str, preco: float):
        self.nome = nome
        self.__localizacao = localizacao # _ _ indica que o atributo eh pvd
        self.__preco = preco
    
    def getnome(self) -> str:
        return self.nome
    
    @property
    def localizacao(self) -> str:
        return self.__localizacao
    
    @localizacao.setter
    def localizacao(self, localizacao):
        self.__localizacao = localizacao
        
    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco
        
    @abstractmethod
    def calcula_area(self) -> float:
        pass
    #criando metodo abstrato calcula_peso, pois cada tipo de terreno vai ter o seu comportamento nesse calculo (a depender do formato do terreno)
    @abstractmethod
    
    def calcula_peso(self) -> float:
        pass

class TerrenoCircular(Terreno):
    def __init__(self, nome: str, localizacao: str, preco: int, raio: int):
        super().__init__(nome,localizacao, preco)
        self.raio = raio

    def calcula_area(self) -> float:
        return self.raio * self.raio * 3.14
    
    def calcula_peso(self) -> float:
        return self.preco / (self.raio * self.raio * 3.14) 
        
class TerrenoRetangular(Terreno):
    def __init__(self, nome: str, localizacao: str, preco: int, ladoMenor: int, ladoMaior: int):
        super().__init__(nome, localizacao, preco)
        self.ladoMenor = ladoMenor
        self.ladoMaior = ladoMaior
        
    def calcula_area(self) -> float:
        return self.ladoMenor * self.ladoMaior
    
    def calcula_peso(self) -> float:
        return self.preco / (self.ladoMenor * self.ladoMaior) 

terreno1 = TerrenoCircular(nome='Circular 1', localizacao = 'centro', preco=70000, raio=15)  
terreno2 = TerrenoRetangular(nome='Retangular', localizacao = 'rural', preco=75000, ladoMenor=20, ladoMaior=35)
terreno3 = TerrenoCircular(nome='Circular2', localizacao = 'rodovia', preco=110000, raio=20)

#Criando lista para armazenar dados que virao abaixo 
lista = []

#Função para adicionar cada objeto "terreno" na lista criada
def adicionar_lista(Terreno):
    lista.append(Terreno)
    print(f'{Terreno.nome} adicionado com sucesso!')

#chamo o metodo para q ele seja executado
adicionar_lista(terreno1)
adicionar_lista(terreno2)
adicionar_lista(terreno3)

# Imprimindo os pesos de cada terreno na lista
for terreno in lista:
    print(f"Terreno: {terreno.nome}, Localizacao: {terreno.localizacao}, Preço: {terreno.preco}, Area: {terreno.calcula_area()}, Peso: {terreno.calcula_peso(): .2f}")

#Função para aencontrar o terreno mais barato
terrenoMenorPeso = min(lista, key=lambda terreno: terreno.calcula_peso())

# Imprimindo os detalhes do terreno mais barato
print(f"O terreno com melhor custo eh: {terrenoMenorPeso.nome} com peso de {terrenoMenorPeso.calcula_peso(): .2f} e preço de {terrenoMenorPeso.preco}")