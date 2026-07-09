limite = int(input("ingresa un numero limite: "))
suma_total = 0
for i in range(1, limite + 1):
    print(i) 
    suma_total += i
print(f"la suma total es: {suma_total}")