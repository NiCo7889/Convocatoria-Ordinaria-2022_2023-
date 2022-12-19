"""
Si escribimos los dígitos de "60" como palabras en inglés, obtenemos "sixzero"; el número de letras en "sixzero" es siete. El número de letras en "siete" es cinco. El número de letras en "cinco" es cuatro. El número de letras en "cuatro" es cuatro: hemos alcanzado un equilibrio estable.

Esto es correcto. Cuando escribimos "60" como palabras en inglés, obtenemos "sixzero", que tiene siete letras. El número de letras en "siete" es cinco, y el número de letras en "cinco" es cuatro. Por lo tanto, al escribir el número "60" como palabras en inglés y contando el número de letras de cada palabra resultante, eventualmente llegamos a un equilibrio en el que el número de letras es igual a cuatro.

 

Nota: para números enteros mayores de 9, escriba los nombres de cada dígito en una sola palabra (en lugar del nombre propio del número en inglés). Por ejemplo, escribe 12 como "unodos" (en lugar de doce) y 999 como "nineninenine" (en lugar de novecientos noventa y nueve).

Para cualquier número entero entre 0 y 999, devuelva una matriz que muestre la ruta desde ese número entero hasta un equilibrio estable:

Ejemplos

numbersOfLetters(60) --> ["sixzero", "seven", "five", "four"]
numbersOfLetters(1) --> ["one", "three", "five", "four"]
"""

from ast import main

def numbersOfLetters(n):
    if n<0 or n>999:
        raise ValueError("Este valos no vale para este ejercicio, El numero tiene que estar en 0 y 999.")
    n = str(n)
    for i in range(len(n)):
       if n[i] == 0:
        n= "zero" + n[i+1:]
       elif n[i] == 1:
        n= "one" + n[i+1:]
       elif n[i] == 2:
        n= "two" + n[i+1:]
       elif n[i] == 3:
        n= "three" + n[i+1:]
       elif n[i] == 4:
        n= "four" + n[i+1:]
       elif n[i] == 5:
        n= "five" + nnum[i+1:]
       elif n[i] == 6:
        n= "six" + n[i+1:]
       elif n[i] == 7:
        n= "seven" + n[i+1:]
       elif n[i] == 8:
        n= "eight" + n[i+1:]
       elif n[i] == 9:
        n= "nine" + n[i+1:]
    return n

print(numbersOfLetters(60))

num = str(60)
for i in range(len(num)):
    if num[i] == "0":
        num = "zero" + num[i+1:]
    elif num[i] == "1":
        num = "one" + num[i+1:]
    elif num[i] == "2":
        num = "two" + num[i+1:]
    elif num[i] == "3":
        num = "three" + num[i+1:]
    elif num[i] == "4":
        num = "four" + num[i+1:]
    elif num[i] == "5":
        num = "five" + num[i+1:]
    elif num[i] == "6":
        num = "six" + num[i+1:]
    elif num[i] == "7":
        num = "seven" + num[i+1:]
    elif num[i] == "8":
        num = "eight" + num[i+1:]
    elif num[i] == "9":
        num = "nine" + num[i+1:]
print(num)

print(numbersOfLetters(7))

if __name__=="__main__":
    main()