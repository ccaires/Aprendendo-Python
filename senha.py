nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while(nome==senha):
    print("Erro. Favor digite a senha diferente do seu nome")
    nome=input()
    senha=input()

print("Cadastro realizado com sucesso")

