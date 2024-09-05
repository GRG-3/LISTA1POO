def obter_numero_notas():
    """Solicita ao usuário o número de notas e valida a entrada."""
    while True:
        try:
            num_notas = int(input("Quantas notas você deseja inserir? "))
            if num_notas > 0:
                return num_notas
            else:
                print("O número de notas deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def obter_nota(indice):
    """Solicita ao usuário uma nota e valida a entrada."""
    while True:
        try:
            nota = float(input(f"Digite a nota {indice + 1} (0 a 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número decimal.")

def calcular_media(soma_notas, num_notas):
    """Calcula a média das notas."""
    return soma_notas / num_notas

def determinar_situacao(media):
    """Determina a situação do aluno com base na média."""
    nota_minima = 7.0
    nota_recuperacao = 5.0
    if media >= nota_minima:
        return "Aprovado"
    elif media >= nota_recuperacao:
        return "Em recuperação"
    else:
        return "Reprovado"

def main():
    print("Bem-vindo ao sistema de cálculo de notas.")

    # Obtendo o número de notas
    num_notas = obter_numero_notas()

    # Coletando as notas e calculando a soma
    soma_notas = 0.0
    for i in range(num_notas):
        nota = obter_nota(i)
        soma_notas += nota

    # Calculando a média
    media = calcular_media(soma_notas, num_notas)

    # Exibindo a média
    print(f"Sua média é: {media:.2f}")

    # Determinando e exibindo a situação
    situacao = determinar_situacao(media)
    print(f"Sua situação é: {situacao}")

if __name__ == "__main__":
    main()
