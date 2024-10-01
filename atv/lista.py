lista = [0] * 5 
cont = 0
maior = float('-inf')
menor = float('inf')

print("Digite um valor para a lista:")
for cont in range (len(lista)):
    valor = int(input(""))
    if valor < menor:
        menor = valor
    if valor > maior:
        maior = valor  
    lista[cont] = valor

#mostrar a lista
print("Lista:", lista)
#mostrar menor e maior:
print(f"O maior é:{maior}")
print(f"O menor é:{menor}")