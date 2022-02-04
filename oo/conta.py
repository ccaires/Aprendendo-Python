class Conta:
	def __init__(self,numero,titular,saldo,limite):
		print("Construindo objeto...{}".format(self))
		self.__numero = numero
		self.__titular = titular
		self.__saldo = saldo
		self.__limite = limite
		
	def extrato(self):
		print("O saldo do titular {} é de {}".format(self.__titular, self.__saldo))

	def depositar(self,valorDeposito):
		self.__saldo += valorDeposito

	def sacar(self,valorSaque):
		self.__saldo -= valorSaque

	def transferir(self,valor,destino):
		self.sacar(valor)
		destino.depositar(valor)

	def get_saldo(self):
		return self.__limite

	
	@property                      #no terminal usar: nomeObj.nomeClasse
	def limite(self):
		return self.__limite

	@limite.setter                #no terminal usar: nomeObj.nomeClasse = valorLimite
	def limite(self,limite):
		self.__limite = limite

	@staticmethod
	def codigo_banco():
		return "001"

	@staticmethod
	def codigos_bancos():
		return {"BB":'001', "Caixa":'104'}

















#ORIENTAÇÕES
#1 - Para criar um objeto, na linha de comando faça o seguinte: nomeDoObj = nomedaClasse(parâmetros a serem passados)
# 2 - Para o depósito, no terminal digite: conta.depositar(digiteOvalor). Após isso, chame a função do extrato e verifique se o valor do saldo alterou. Ex: conta.extrato()
# 3 - Para tranferir: nomedoObj.transferir(numeralValor, nomeDoObjDestino). Feito isso, basta consultar o extrato de cada um e saber o valor do saldo dos mesmos.
