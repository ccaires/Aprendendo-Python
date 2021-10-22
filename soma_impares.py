num = int(input())
x = int(input())
y = int(input())
z=0
#i=0
w=0
aux=0
soma=0
lista = []

while z!=num:
    if(x>y):
        aux=x
        x=y
        y=aux
    j=x
    k=y-x
    
    for i in range(k+1):
        lista.append(j)
        j=j+1
    print(lista)

    i = 1
   
   #Nesse for o valor não deve ser iniciado no i=0 e sim no i=1 e assim ir incrementando::::COMO FAZER???
    for i in range (k):
        if(lista[i]%2 != 0):
            soma=soma+lista[i]
            print(lista)
            
    print(soma)
    soma=0
    z=z+1
    del lista[:]
    print(lista)
    x=int(input())
    y=int(input())

