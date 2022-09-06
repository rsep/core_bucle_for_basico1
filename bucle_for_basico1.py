# 1: BÁSICO
print("Básico")
for x in range(151):
    print(x)

# 2: MÚLTIPLOS DE 5
print("\nMúltiplos de 5")
for i in range(5,1001):
    if i % 5 == 0:
        print(i)

# 3: CONTAR A LA MANERA DE DOJO
print("\nContar a la manera de Dojo")
for y in range(1,101):
    if y % 5 == 0:
        if y % 10 == 0:
            print("Coding Dojo")
        else:
            print("Coding")
    else:
        print(y)

# 4: WHOA ES UN GRAN IDIOTA
print("\nWhoa. Es un gran idiota")
suma = 0
for impar in range(500000+1):
    if (impar % 2 != 0):
        suma = suma + impar
print(suma)
print(f'(Con formato de número) La suma es: {suma:,.0f}')


# 5: CUENTA REGRESIVA DE A 4
print("\nCuenta regresiva de a 4")
year = 2018
for num in range(1,year+1):
    print(year)
    year = year -4
    if year < 0:
        break

# 6: CONTADOR FLEXIBLE
print("\nContador Flexible")
lowNum = 2
highNum = 9
mult = 3
for numero in range(lowNum, highNum+1):
    if numero % mult == 0:
        print(numero)
