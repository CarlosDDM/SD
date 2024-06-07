import Pyro4

# Cria um proxy para se conectar ao servidor Pyro
def main():
    calculadora = Pyro4.Proxy("PYRO:obj_be1f91d86eb840edb3731cc532827e95@localhost:61630")  # Substitua 'obj_123456' pelo URI do servidor
    resultado = calculadora.somar(85, 3)
    print("A soma é:", resultado)

    resultado = calculadora.subtracao(85, 3)
    print(f"A subtração é: {resultado}")

    resultado = calculadora.multiplicacao(85, 3)
    print(f"A multiplicação é: {resultado}")

    resultado = calculadora.divisao(85, 3)
    print(f"A divisão é: {resultado}")


if __name__ == "__main__":
    main()
