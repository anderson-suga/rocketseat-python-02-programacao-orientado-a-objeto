"""
    A POO é um paradigma de programação que se baseia na organização dos programas em torno de objetos, que são instâncias de classes. 
    As classes são modelos que definem a estrutura e o comportamento dos objetos. 
    Dentro das classes, podemos descrever atributos e métodos, que são as ações que os objetos podem realizar. 
    O construtor é um método especial que nos permite definir os atributos da classe.
"""

"""
    Os objetos são criados a partir de uma classe e possuem os mesmos atributos e métodos definidos na classe. 
    Os atributos são os dados da classe, enquanto os métodos são as funções que a classe pode ter. 
    Os objetos podem representar entidades do mundo real, como pessoas, carros, contas bancárias, etc. 
    Para criar um objeto, definimos uma variável que recebe uma instância da classe, passando os valores dos atributos necessários.
    Podemos acessar os atributos do objeto utilizando a notação de ponto. 
    Também podemos adicionar métodos à classe para realizar ações específicas. 
    Os objetos criados a partir da classe podem chamar esses métodos. 
    A programação orientada a objetos oferece vantagens como reutilização de código, organização e estrutura, 
    além dos pilares do PO: encapsulamento, herança, polimorfismo e abstração. 
    No entanto, também apresenta desvantagens, como complexidade e curva de aprendizado.
"""


# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade


# Objetos
pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa(nome="Rodrigo", idade=32)
mensagem = pessoa2.saudacao()
print(mensagem)
