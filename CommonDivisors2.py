numero1 = int(input("Dime el primer numero:"))
numero2 = int(input("Dime el segundo numero:"))
count1 = 1
lista = []
while count1 <= numero1 or count1 <= numero2:
  if numero1 % count1 == 0 and numero2 % count1 == 0:
    lista.append(count1)
  count1 = count1 +1
  
for numero in lista:
  print(numero)