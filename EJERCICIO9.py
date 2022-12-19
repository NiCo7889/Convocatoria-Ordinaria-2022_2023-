"""
¡A nadie le gustan los lunes! Pasaste el fin de semana de fiesta y con amigos, y luego llega el lunes y tienes que levantarte temprano, ponerte ropa de negocios e ir a trabajar. Entonces, ¿cuántos de estos horribles días tiene que soportar alguien? Bueno, averigüémoslo.

Cree un método para encontrar el número de lunes dado el cumpleaños de una persona y la fecha actual. Para este ejercicio simple, no te preocupes por los días festivos/vacaciones, licencia por enfermedad, etc. Supongamos que una persona tiene un trabajo y va a trabajar durante todo el año si está en edad de trabajar. Para simplificar las cosas, suponga que alguien comienza a trabajar cuando tiene 22 años y se jubila cuando tiene 78.

¡Así es, los lunes no cuentan cómo días malos si estás en la escuela/universidad o eres jubilado!

En las pruebas, la fecha actual será la misma o posterior al cumpleaños de una persona y ambas fechas serán no nulas y válidas. Y aunque no tener que trabajar los fines de semana es una moda bastante reciente (¡búscalo!), asume que los lunes siempre serán y serán días malos en cualquier época.

Para resolver este problema, se puede seguir los siguientes pasos:

Calcular la edad de la persona en la fecha actual. Para ello, se puede calcular la diferencia en años entre la fecha actual y la fecha de cumpleaños de la persona.
Verificar si la persona está en edad de trabajar. Para ello, se puede comprobar si su edad está entre 22 y 78 años.
Calcular el número de lunes que hay entre la fecha de cumpleaños y la fecha actual. Para ello, se puede calcular el número de días que hay entre ambas fechas y dividirlo por 7, ya que una semana tiene 7 días.
Si la persona está en edad de trabajar, devolver el número de lunes calculado en el paso 3. En caso contrario, devolver 0.
"""
from ast import main 

def contador_lunes(cumple, actual):
    dias = actual - cumple
    semanas = dias.days // 7
    lunes = semanas + 1
    return lunes

from datetime import date

def unlucky_days(birthday, current_date):
    #calcular la diferencia en años entre la fecha actual y la fecha de cumpleaños de la persona.
    edad = current_date.year- birthday.year
    # ver si la persona está en edad de trabajar
    if edad >= 18 and edad <= 75:
        #calcular el número de lunes que hay entre la fecha de cumpleaños y la fecha actual
        lunes = contador_lunes(birthday, current_date)
        return lunes
    else:
        return 0

print(unlucky_days(date(2012, 4, 4), date(2015, 2, 1)))




if __name__ == '__main__':
    main()