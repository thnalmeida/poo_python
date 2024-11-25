#TRABALHO 03 - POO 2024/2

from abc import ABC, abstractmethod #itens necessaios para criar classes abstratas

#Definindo classe abstrata EmpDomestica
class EmpDomestica(ABC):
    def __init__(self, nome: str, telefone: int, almoco: bool):
        self.__nome = nome
        self.__telefone = telefone
        self.almoco = almoco


    #para colocar um metodo privado
    @property
    def nome(self):
        return self.__nome

    @property
    def telefone(self) -> int:
        return self.__telefone
    
    @abstractmethod
    def getSalario(self):
        pass
    

    '''um método abstrato é um método que é declarado em uma classe base 
    (ou classe abstrata), mas não possui implementação. 
    Esse tipo de método define o que as subclasses devem fazer, 
    mas deixa para elas a responsabilidade de definir como elas vão fazer. '''
    #são comuns em designs de sistemas que exigem que várias subclasses
    #implementem suas próprias versões de uma ação específica.
    #Nesse caso, cada modalidade de empregada domestica tem uma forma de calcular o salario. ou seja, 
    #cada uma vai implementar o método (salario) à sua maneira dentro da classe. herdando o método da classe mae.

#Definindo subclasse Horista (superclasse: EmpDomestica) 
#Adiciono atributos que ela vai ter e q nao tem na super classe
class Horista(EmpDomestica): 
    def __init__(self, nome: str, telefone: int, almoco: bool, horasTrabalhadas: float, valorPorHora: float):
        super().__init__(nome, telefone, almoco)
        self.horasTrabalhadas = horasTrabalhadas
        self.valorPorHora = valorPorHora
        self.almoco = almoco
    
    def getSalario(self) -> float:
        return self.horasTrabalhadas * self.valorPorHora

class Diarista(EmpDomestica):
    def __init__(self, nome: str, telefone: int, almoco: bool, diasTrabalhados: int, valorPorDia: float):
        super().__init__(nome, telefone, almoco)
        self.diasTrabalhados = diasTrabalhados
        self.valorPorDia = valorPorDia

    def getSalario(self) -> float:
        return self.diasTrabalhados * self.valorPorDia
    
class Mensalista(EmpDomestica):
    def __init__(self, nome: str, telefone: int, almoco: bool, valorMensal: float):
        super().__init__(nome, telefone, almoco)
        self.valorMensal = valorMensal

    def getSalario(self) -> float:
        return self.valorMensal

#lista para adicionar dados que virao abaixo: 
lista = []

#Função para adicionar pessoa na lista
def adicionar_pessoa(EmpDomestica):
    lista.append(EmpDomestica)
    print(f"{EmpDomestica.nome} foi cadastrada com sucesso!")
    
empregada1 = Horista(nome='Ana', telefone=35984184074, almoco='false', horasTrabalhadas=160, valorPorHora=12)
empregada2 = Diarista(nome='Betina', telefone=35974002817,almoco='true', diasTrabalhados=20, valorPorDia=65)
empregada3 = Mensalista(nome='Catarine', telefone=35984387366,almoco='false', valorMensal=1200)

adicionar_pessoa(empregada1)
adicionar_pessoa(empregada2)
adicionar_pessoa(empregada3)

#Imprimir dados dos salarios de cada uma: 
for empregada in lista:
    print(f"Nome = {empregada.nome}, Salario Mensal= {empregada.getSalario()}")

#Função para encontrar empregada mais barata:
empregadaMaisBarata = min(lista, key=lambda empregada: empregada.getSalario())

#funcao para imprimir dados da mais barata
print(f"Empregada mais barata: {empregadaMaisBarata.nome}, {empregadaMaisBarata.telefone}, Preço: {empregadaMaisBarata.getSalario()}")


