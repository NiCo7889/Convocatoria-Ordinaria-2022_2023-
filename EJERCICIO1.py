"""
Para este ejercicio, creará un solucionador de Nonogramas. :)

Si no sabe qué son los nonogramas, puede consultar algunas instrucciones y también probar algunos nonogramas aquí.

Para resolver un Nonograma, primero debemos entender cómo funcionan. Un Nonograma es un rompecabezas que consta de una matriz de celdas en blanco y negro. Las pistas se proporcionan en los bordes de la matriz en forma de números que indican cuántas celdas negras hay en cada fila o columna consecutiva.

Por ejemplo, si las pistas para una fila son [2, 1], significa que hay dos grupos de celdas negras consecutivas en esa fila, el primero con dos celdas y el segundo con una sola celda. La solución para esta fila sería "BB_X_B" (donde "B" representa una celda negra y "X" representa una celda en blanco).

Para resolver un Nonograma completo, debemos usar las pistas y nuestro conocimiento de cómo funcionan los Nonogramas para ir rellenando la matriz poco a poco hasta obtener la solución final.

solo tendrás que resolver Nonogramas 5x5. :)

Instrucciones
Necesitas completar la clase Nonogram y el método solve:

class Nonogram:

 

    def __init__(self, clues):

        pass

 

    def solve(self):

        pass

Se te darán las pistas y deberás devolver el rompecabezas resuelto. Todos los acertijos se podrán resolver, por lo que no tendrás que preocuparte por eso. Habrá exactamente una solución para cada rompecabezas.

Las pistas serán una tupla de las pistas de columna, luego las pistas de fila, que contendrán las pistas individuales. Por ejemplo, para el Nonograma:

    |   |   | 1 |   |   |

    | 1 |   | 1 |   |   |

    | 1 | 4 | 1 | 3 | 1 |

-------------------------

  1 |   |   |   |   |   |

-------------------------

  2 |   |   |   |   |   |

-------------------------

  3 |   |   |   |   |   |

-------------------------

2 1 |   |   |   |   |   |

-------------------------

  4 |   |   |   |   |   |

-------------------------

Las pistas están en la parte superior e izquierda del rompecabezas, así que en este caso:

Las pistas de columna son: ((1, 1), (4,), (1, 1, 1), (3,), (1,)), y las pistas de fila son: ((1,), (2,), (3,), (2, 1), (4,)). Las pistas de la columna se dan de izquierda a derecha. Si hay más de una pista para la misma columna, la pista superior se da primero. Las pistas de fila se dan de arriba a abajo. Si hay más de una pista para la misma fila, la pista más a la izquierda se da primero.
Por lo tanto, la pista dada al __init__método sería (((1, 1), (4,), (1, 1, 1), (3,), (1,)), ((1,), (2,), (3,), (2, 1), (4,))). Se le dan las pistas de la columna primero y luego las pistas de la fila en segundo lugar.
Debe devolver una tupla de las filas como su respuesta. En este caso, el Nonograma resuelto se ve así:

    |   |   | 1 |   |   |

    | 1 |   | 1 |   |   |

    | 1 | 4 | 1 | 3 | 1 |

-------------------------

  1 |   |   | # |   |   |

-------------------------

  2 | # | # |   |   |   |

-------------------------

  3 |   | # | # | # |   |

-------------------------

2 1 | # | # |   | # |   |

-------------------------

  4 |   | # | # | # | # |

-------------------------

En la tupla, debe usar 0 para un cuadrado vacío y 1 para un cuadrado lleno. Por lo tanto, en este caso, debe devolver:

((0, 0, 1, 0, 0),

 (1, 1, 0, 0, 0),

 (0, 1, 1, 1, 0),

 (1, 1, 0, 1, 0),

 (0, 1, 1, 1, 1))
"""

class Nonogram:
    
        def __init__(self, clues):
            self.clues = clues
            self.columnas = clues[0]
            self.filas = clues[1]
            self.nonograma = []
            for i in range(len(self.columnas)):
                self.nonograma.append([0]*len(self.columnas))
            self.nonograma = tuple(self.nonograma)
    
        def solve(self):
            self.rellenar()
            self.rellenar2()
            self.rellenar3()
            self.rellenar4()
            self.rellenar5()
            self.rellenar6()
            self.rellenar7()
            self.rellenar8()
            self.rellenar9()
            self.rellenar10()
            self.rellenar11()
            self.rellenar12()
            self.rellenar13()
            self.rellenar14()
            self.rellenar15()
            self.rellenar16()
            self.rellenar17()
            self.rellenar18()
            self.rellenar19()
            self.rellenar20()
            self.rellenar21()
            self.rellenar22()
            self.rellenar23()
            self.rellenar24()
            self.rellenar25()
            self.rellenar26()
            self.rellenar27()
            self.rellenar28()
            self.rellenar29()
            self.rellenar30()
            self.rellenar31()
            self.rellenar32()
            self.rellenar33()
            self.rellenar34()
            self.rellenar35()
            self.rellenar36()
            self.rellenar37()
            self.rellenar38()
            self.rellenar39()
            self.rellenar40()
            self.rellenar41()
            self.rellenar42()
            self.rellenar43()
            self.rellenar44()
            self.rellenar45()
            self.rellenar46()
            self.rellenar47()
            self.rellenar48()
            self.rellenar49()
            self.rellenar50()
            self.rellenar51()
            self.rellenar52()
            self.rellenar53()
            self.rellenar54()
            self.rellenar55()
            self.rellenar56()
            self.rellenar57()
            self.rellenar58()
            self.rellenar59()
            self.rellenar




            return self.nonograma

        def rellenar(self):
            for i in range(len(self.columnas)):
                if len(self.columnas[i]) == 1:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                elif len(self.columnas[i]) == 2:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 3:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 4:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][3]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 5:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][3]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][4]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 6:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][3]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][4]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][5]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 7:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][3]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][4]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][5]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][6]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 8:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][3]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][4]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][5]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][6]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][7]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 9:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][3]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][4]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][5]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][6]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][7]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][8]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 10:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][3]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][4]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][5]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][6]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][7]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][8]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][9]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 11:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][3]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][4]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][5]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][6]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][7]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][8]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][9]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][10]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                elif len(self.columnas[i]) == 12:
                    for j in range(self.columnas[i][0]):
                        self.nonograma[j][i] = 1
                    for j in range(self.columnas[i][1]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][2]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][3]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][4]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][5]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][6]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][7]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][8]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][9]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][10]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1
                    for j in range(self.columnas[i][11]):
                        self.nonograma[len(self.columnas[i])-j-1][i] = 1