n=int(input("Digite um número: "))

while (n>=0):
    if (n>=0 and n<=10):
        print("O número digitado foi:",n)
        break
    else:
        print("Número inválido. Digite um número entre 0 e 10.")
        n=int(input())

