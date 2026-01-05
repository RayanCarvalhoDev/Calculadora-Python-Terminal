# Mensagem inicial exibida quando o programa começa
print("Olá, Bem-vindo a calculadora =)")

# =========================
# FUNÇÃO: entradaUsuario
# Responsável por:
# - pedir os números ao usuário
# - validar se são números
# - validar o operador
# - retornar os dados corretos
# =========================
def entradaUsuario():
    # Lista de operadores permitidos
    operadores = ["+", "-", "x", "/"]

    # Loop infinito: só sai quando os dados forem válidos
    while True:
        try:
            # Solicita o primeiro número
            num1 = int(input("Digite o primeiro número: "))

            # Solicita o segundo número
            num2 = int(input("Digite o segundo número: "))
        except ValueError:
            # Executado se o usuário digitar algo que não seja número
            print("Por favor, digite apenas números!")
            continue  # volta para o início do loop
        
        # Solicita o operador da operação
        opcao = input("Seleciona o operador ([+] [-] [x] [/]): ")
    
        # Verifica se o operador digitado é válido
        if opcao not in operadores:
            print("Operador Invalido!")
            continue  # volta para o início do loop

        # Retorna os dados para o programa principal
        # O return encerra a função
        return num1, opcao, num2


# =========================
# FUNÇÃO: calcularExibir
# Responsável por:
# - receber os valores
# - realizar o cálculo
# - exibir o resultado
# =========================
def calcularExibir(num1, opcao, num2):

    # Caso o operador seja soma
    if opcao == "+":
        print(f"O Resultado de {num1} {opcao} {num2} é {(num1 + num2)}")

    # Caso o operador seja subtração
    elif opcao == "-":
        print(f"O Resultado de {num1} {opcao} {num2} é {(num1 - num2)}")

    # Caso o operador seja multiplicação
    elif opcao == "x":
        print(f"O Resultado de {num1} {opcao} {num2} é {(num1 * num2)}")

    # Caso o operador seja divisão
    elif opcao == "/":
        # Verifica se o divisor é zero
        if num2 == 0:
            print("Erro: divisão por zero não é permitida!")
        else:
            print(
                f"O Resultado de {num1} {opcao} {num2} é {round(num1 / num2, 2)}"
            )


# =========================
# PROGRAMA PRINCIPAL
# Aqui o código:
# - chama as funções
# - controla a repetição da calculadora
# =========================
while True:
    # Recebe os dados retornados pela função de entrada
    num1, num2, opcao = entradaUsuario()

    # Envia os dados para a função que calcula e exibe
    calcularExibir(num1, num2, opcao)

    # Pergunta ao usuário se deseja continuar
    if input("Deseja fazer outro cálculo? (s/n): ").lower() != "s":
        break  # Encerra o loop e finaliza o programa
