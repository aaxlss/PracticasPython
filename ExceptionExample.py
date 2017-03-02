from Exceptions.Numbers import Numbers

n = Numbers()

try:

    num1, num2 = input("Introduce dos numeros separados por comas:")

except NameError:

    print("No se ingresaron numeros.")
    raise

except TypeError:

    print("No se indicaron los numeros separados por comas")

else:
    print("Solo se ejecuta cuando no entra a nigun except")

finally:
    print("Siempre se ejecuta finally")

print(n.sum(num1, num2))