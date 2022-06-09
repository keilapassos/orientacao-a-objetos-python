# Classe 'original'

# class SistemaCadastral:

#     def cadastrar(self, nome: str, idade: int) -> None:
#         if isinstance(nome, str) and isinstance(idade, int):
#             print('acessando o banco de dados...')
#             print(f'Cadastrar o usuário {nome}, idade {idade}')
#         else:
#             print('dados inválidos')

# Reformulando a classe para o princípio de Responsabilidade Única do SOLID (S)


class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_dados(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        return False

    def __armazenar_dados(self, nome: str, idade: int) -> None:
        print("Acessando o banco de dados...")
        print(f"Cadastrar o usuário {nome}, idade {idade}")

    def __indicar_erro(self) -> None:
        print("Dados inválidos")
