num = int(input())

ano=num//365
meses=(num%365)//30
dias=(num%365)%30

print(ano, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")

