a = int(input())
b = int(input())
c = int(input())
maior = 0
meio = 0
menor = 0

if (a>b):
    maior = a
    meio = b
    menor = c
    if (b<c):
        meio = c
        menor = b
        if (c>a):
            maior = c
            meio = a
elif (a>c):
    maior = a
    meio = b
    menor = c
    if (b<c):
        meio = c
        menor = b
        if (c>a):
            maior = c
            meio = a
elif (b>a):
    maior = b
    meio = a
    menor = c
    if (a<c):
        meio = c
        menor = a
        if (c>b):
            maior = c
            meio = b
elif (b>c):
    maior = b
    meio = a
    menor = c
    if (a<c):
        meio = c
        menor = a
        if(c>b):
            maior = c
            meio = b
elif (c>a):
    maior = c
    meio = a
    menor = b
    if (a<b):
        meio = b
        menor = a
        if (b>c):
            maior = b
            meio = c
elif (c>b):
    maior = c
    meio = a 
    menor = b
    if (a<b):
        meio = b
        menor = a
        if (b>c):
            maior = b
            meio = c

print(maior,meio,menor)


