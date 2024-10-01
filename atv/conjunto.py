matriz = [
    [0,0,0], 
    [0,0,0], 
    [0,0,0]
]

c = 0

while c < len(matriz[0]):
    l = 0
    while l < len(matriz):
        matriz[l][c] = int(input(f"Informe um valor matriz[{l}][{c}]: "))
        l+=1
    c+=1

print(matriz)
