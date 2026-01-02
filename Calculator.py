operadores = ["+", "-", "x", "/"]

print("Olá, Bem-vindo a calculadora =)")

while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite apenas números!")
        continue
        
    opcao = input("Seleciona o operador ([+] [-] [x] [/]): ")
    
    if opcao not in operadores:
        print("Operador Invalido!")
        continue
        

    if opcao == "+":
        print(f"O Resultado de {num1} {opcao} {num2} é {(num1 + num2)}")
    elif opcao == "-":
        print(f"O Resultado de {num1} {opcao} {num2} é {(num1 - num2)}")
    elif opcao == "x":
        print(f"O Resultado de {num1} {opcao} {num2} é {(num1 * num2)}")
    elif opcao == "/":
        if num2 == 0:
            print("Erro: divisão por zero não é permitida!")
        else:
            print(f"O Resultado de {num1} {opcao} {num2} é {round(num1 / num2, 2)}")
        
    continuar = input("Deseja fazer outro calculo? (s/n): ")
    if continuar.lower() != "s":
        break
        

    