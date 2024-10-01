t = ("maçã", "banana", "laranja", "abacaxi", "uva")

f = input("Digite uma fruta:")
if f in t:
    print(f"A fruta {f} existe na tupla")
else:
    print(f"A fruta {f} não existe na tupla")