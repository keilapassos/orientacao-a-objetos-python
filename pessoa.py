class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf  # atibuto privado, acessado apenas no contexto da classe

    def beber(self, bebida):
        alcoolicos = ["cerveja", "vinho", "whisky", "tequila", "vodka"]

        if bebida.lower() in alcoolicos:
            print("Apresente o cpf")
            return self.__mostrar_cpf()

        print(f"Bebendo {bebida}")

    def __mostrar_cpf(
        self,
    ):  # método privado, não pode ser acessado fora do contexto da classe
        print(self.__cpf)


ronaldo = Pessoa("Ronaldo", 32, "fd4gf5gd4gf")
ronaldo.beber("coca-cola")
ronaldo.beber("Tequila")
