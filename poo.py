"""
    A POO é um paradigma de programação que se baseia na organização dos programas em torno de objetos, que são instâncias de classes. 
    As classes são modelos que definem a estrutura e o comportamento dos objetos. 
    Dentro das classes, podemos descrever atributos e métodos, que são as ações que os objetos podem realizar. 
    O construtor é um método especial que nos permite definir os atributos da classe.
"""


# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
