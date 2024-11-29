#TRABALHO 05 - FOLHA DE PAGAMENTO

#importando bliblioteca abc
from abc import ABC, abstractmethod

#criando classe abstrata Funcionario (nao pode ser instanciada diretamente) 
class Funcionario(ABC): #(ABC) indica que a classe eh abstrata
    def __init__(self, codigo: int, nome: str):
        self.codigo = codigo 
        self.nome = nome
    
    def adicionaPonto(self, mes, ano, nroFaltas, horaAtrasos):
        self.mes = mes
        self.ano = ano
        self.nroFaltas = nroFaltas
        self.horaAtrasos = horaAtrasos
        
    def lancaFaltas(self, mes: int, ano:int, nroFaltas: int):
        self.mes = mes
        self.ano = ano
        self.nroFaltas = nroFaltas
        
    def lancaAtrasos(self, mes: int, ano:int, horaAtrasos: int):
        self.mes = mes
        self.ano = ano
        self.horaAtrasos = horaAtrasos
    
    #coloco o @abstracmethod para indicar que as classes filhas obrigatoriamente terao esse metodo e aplicarao à sua maneira (cada uma tera seu calculo de bonus)
    @abstractmethod
    def calculaBonus(self):
        pass
    
    @abstractmethod
    def calculaSalario(self):
        pass
    
    @abstractmethod
    def imprimeFolha(self, mes: int, ano: int):
        pass
        
    
#criando instancia professor
class Professor(Funcionario):
    def __init__(self, codigo: int, nome: str, titulacao: str, salarioHora: float, nroAulas: int):
        super().__init__(codigo, nome)
        #acrescento atributos q sao apenas de Professor:
        self.titulacao = titulacao
        self.salarioHora = salarioHora
        self.nroAulas = nroAulas
        
    def calculaSalario(self):
        self.salarioProf = (self.salarioHora * self.nroAulas) - (self.salarioHora * self.nroFaltas)
        return self.salarioProf
    
    def calculaBonus(self):
        if self.horaAtrasos == 0:
            self.bonus = self.salarioProf * (0.1)
            return self.bonus
        
        if self.horaAtrasos > 0:
            self.bonus = self.salarioProf * (0.1 - (self.horaAtrasos * 0.01))
            return self.bonus
           
    def imprimeFolha(self, mes: int, ano: int):
        self.mes = mes
        self.ano = ano
        print("Codigo: ", self.codigo)
        print("Nome: ", self.nome)
        print(f"Salario líquido: {self.calculaSalario(): .2f}")
        print(f"Bônus: {self.calculaBonus(): .2f}")
     
#criando instancia tecnico admnistrativo
class TecAdmin(Funcionario):
    #acrescento todos os atributos do objeto (aqueles q vieram da superclasse e aqueles q sao especificos do obj):
    def __init__(self, codigo: int, nome: str, funcao: str, salarioMensal: str):
        #defino quais vêm da superclasse
        super().__init__(codigo, nome)
        #declaro qual eh especifico
        self.funcao = funcao
        self.salarioMensal = salarioMensal
        
    def calculaSalario(self):
        self.salarioTec = self.salarioMensal - ((self.salarioMensal/30) * self.nroFaltas)
        return self.salarioTec
    
    def calculaBonus(self):
        if self.horaAtrasos == 0:
            self.bonus = self.salarioTec * (0.08)
            return self.bonus
        
        if self.horaAtrasos > 0:
            self.bonus = self.salarioTec * (0.08 - (self.horaAtrasos * 0.01))
            return self.bonus
        
    def imprimeFolha(self, mes: int, ano: int):
        self.mes = mes
        self.ano = ano
        print("Codigo: ", self.codigo)
        print("Nome: ", self.nome)
        print(f"Salario líquido: {self.calculaSalario(): .2f}")
        print(f"Bônus:  {self.calculaBonus(): .2f}")


if __name__ == "__main__":
#crio lista para adicionar os funcionarios q for adicionando
 funcionarios = []
 
#crio um objeto professor
 prof = Professor(1, "Joao", "Doutor", 45.35, 32) 
 prof.adicionaPonto(4, 2021, 0, 0)
 prof.lancaFaltas(4, 2021, 2)
 prof.lancaAtrasos(4, 2021, 3)
 
 #adiciono esse objeto na lista funcionarios
 funcionarios.append(prof)
 
 #crio um objeto tecnico 
 tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
 tec.adicionaPonto(4, 2021, 0, 0)
 tec.lancaFaltas(4, 2021, 3)
 tec.lancaAtrasos(4, 2021, 4)
 
 #adiciono esse objeto na lista funcionarios
 funcionarios.append(tec)
 
 for func in funcionarios:
    func.imprimeFolha(4, 2021)
    print()