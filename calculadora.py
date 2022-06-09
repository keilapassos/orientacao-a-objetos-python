class Calculadora:
    def calcular(self, operacao, num1, num2):
        if operacao == "+":
            return self.__adicionar(num1, num2)
        elif operacao == "-":
            return self.__subtrair(num1, num2)
        else:
            return f"Operação Inválida com sinal de {operacao}"

    def __adicionar(self, num1, num2):
        return f"Resultado da soma: {num1 + num2}"

    def __subtrair(self, num1, num2):
        return f"Resultado da subtração: {num1 - num2}"


# calculadora = Calculadora()  # sem argumentos pois não tem o __init__
# resultado = calculadora.calcular("+", 2, 2)
# print(resultado)

# resultado = calculadora.calcular("-", 2, 2)
# print(resultado)

# resultado = calculadora.calcular("/", 2, 2)
# print(resultado)

# resultado = calculadora.calcular("*", 2, 2)
# print(resultado)
