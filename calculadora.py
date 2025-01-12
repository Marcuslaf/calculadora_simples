def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        escolha = input("Digite a opção (1/2/3/4/5): ")

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")

            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")

            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")

            elif escolha == '4':
                print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")

        elif escolha == '5':
            print("Encerrando a calculadora!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calculadora()