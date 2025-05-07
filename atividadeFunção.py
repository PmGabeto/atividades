# Função que verifica se um número é primo
def eh_primo(n):
    if n <= 1:
        return False
    for n in range(2, int(i**0.5) + 1):  # Testa divisores até a raiz quadrada de n
        if n % i == 0:
        return False
    return True

# Função principal
def main():
    numero = int(input("Digite um número inteiro: "))
    
    if eh_primo(numero):
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")

# Executa a função principal
main()
