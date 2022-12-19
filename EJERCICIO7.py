"""
Dadas dos posiciones diferentes en un tablero de ajedrez, encuentre el menor número de movimientos que le tomaría a un caballo pasar de una a la otra. Las posiciones se pasarán como dos argumentos en notación algebraica. 

Por ejemplo, knight("a3", "b5")debería devolver 1.

El caballo no puede moverse fuera del tablero. El tablero es de 8x8.

Para resolver este problema, podemos seguir los siguientes pasos:

Convertimos las posiciones de notación algebraica a coordenadas (fila, columna) en un tablero de 8x8. Por ejemplo, la posición "a3" se convertiría a (3, 1) donde 3 es la fila y 1 es la columna.
Creamos una matriz de 8x8 que represente el tablero de ajedrez, y marcamos las posiciones inicial y final con un valor especial (por ejemplo, 0 y 1).
Utilizamos un algoritmo de búsqueda como BFS (Breadth-First Search) para encontrar el camino más corto entre la posición inicial y final. La búsqueda se realiza desde la posición inicial y se expande en todas las posibles posiciones a las que el caballo puede moverse. Cada vez que se encuentra una posición válida (es decir, que está dentro del tablero y no ha sido visitada antes), se agrega a la cola de búsqueda, para nuestro caso una lista. La búsqueda termina cuando se encuentra la posición final o se agota la cola de búsqueda(lista) sin encontrarla.
El número de movimientos requeridos se calcula como la longitud del camino encontrado menos 1 (ya que la posición inicial se cuenta como un movimiento).
 

Para obtener información sobre los movimientos del caballo, consulte https://en.wikipedia.org/wiki/Knight_%28chess%29

Para obtener información sobre la notación algebraica, consulte https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

(Advertencia: muchas de las pruebas se generaron aleatoriamente. Si alguna no funciona, los casos de prueba devolverán la entrada, la salida y la salida esperada; publíquelos).
"""

from ast import main 

def knight(pos1, pos2):
    # your code here
    pass


if __name__ == '__main__':
    main()