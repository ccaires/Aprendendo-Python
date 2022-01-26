import random

print("***********************************")
print("******* Jogo de adivinhação *******")
print("***********************************")

print("\n")

numero_secreto = random.randrange(1,101)
pontos = 1000

print("Níveis de dificuldade: (1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Escolha um nível de dificuldade: "))
tentativas = 0


if(nivel==1):
	tentativas = 20
elif(nivel==2):
	tentativas=10
else:
	tentativas=5

for rodada in range(1, tentativas+1):
	print("Tentativas{} de {}".format(rodada,tentativas))
	chute=int(input("Digite um número entre 1 e 100: "))

	if(chute < 1 or chute > 100):
		print("Você deve digitar um número entre 1 e 100")
		continue

	acertou = chute == numero_secreto
	maior = chute > numero_secreto
	menor = chute < numero_secreto

	if(acertou):
		print("Você acertou. Fez {} pontos".format(pontos))
		break
	else:
		if(maior):
			print("Você errou. Seu número foi maior que o número secreto")
		elif(menor):
			print("Você errou. Seu número foi menor que o número secreto")

		pontos_perdidos = abs(numero_secreto - chute)
		pontos = pontos - pontos_perdidos
	
print("Fim de Jogo!")
