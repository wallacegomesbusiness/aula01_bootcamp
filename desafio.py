# Solicita ao usuário que digite seu nome
digite_seu_nome = input("Digite seu nome: ")


# 2) solicite ao usuário que digite o valor do seu salário
# Converter a entrada para um número de ponto flutuante
salario = float(input("Digite seu salário: "))

# 0) Valor com variavel bonus
def valor_bonus():
    if salario <= 2000:
        return 0.8
    elif salario <= 5000:
        return 1.2
    elif salario <= 10000:
        return 1.5

# 3) Solicite ao usuário que digite o valor do bônus recebido
# Converter a entrada para um número de ponto flutuante
# bonus = float(input("Digite o valor do seu bônus: "))

# 4) Calculo o valor do bônus final
valor_bonus = valor_bonus() * salario 

# 5) Imprima cálculo do KPI para o usuário
# print(valor_bonus)

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e o bônus
print(f"O usuário {digite_seu_nome} possui o bonus de {valor_bonus}")

