import Teclado
import BubbleSort

def ejemplo_enteros():
    # Ordena lista de enteros
    cantidad = Teclado.Teclado.read_integer("¿Cuántos números enteros deseas ordenar?", min_value=1)
    lista = []
    for i in range(cantidad):
        numero = Teclado.Teclado.read_integer(f"Ingrese el número entero #{i + 1}:")
        lista.append(numero)

    print("Lista original:", lista)
    lista_ordenada = BubbleSort.bubble_sort(lista.copy()) # Ordena la lista
    print("Lista ordenada (ascendente):", lista_ordenada)


def ejemplo_flotantes():
    # Ordena lista de decimales
    cantidad = Teclado.Teclado.read_integer("¿Cuántos números decimales deseas ordenar?", min_value=1)
    lista = []
    for i in range(cantidad):
        numero = Teclado.Teclado.read_double(f"Ingrese el número decimal #{i + 1}:")
        lista.append(numero)

    print("Lista original:", lista)
    lista_ordenada = BubbleSort.bubble_sort(lista.copy()) # Ordena la lista
    print("Lista ordenada (ascendente):", lista_ordenada)


def ejemplo_textos():
    # Ordena lista de textos
    cantidad = Teclado.Teclado.read_integer("¿Cuántas palabras o textos deseas ordenar?", min_value=1)
    lista = []
    for i in range(cantidad):
        texto = Teclado.Teclado.read_text(f"Ingrese el texto #{i + 1}:", min_length=1)
        lista.append(texto)

    print("Lista original:", lista)
    # Ordena alfabéticamente
    lista_ordenada = BubbleSort.bubble_sort(lista.copy(), key=lambda x: x.lower())
    print("Lista ordenada alfabéticamente:", lista_ordenada)


def ejemplo_personas():
    # Ordena lista de personas
    cantidad = Teclado.Teclado.read_integer("¿Cuántas personas deseas ingresar?", min_value=1)
    personas = []
    for i in range(cantidad):
        nombre = Teclado.Teclado.read_text(f"Ingrese el nombre de la persona #{i + 1}:", min_length=1)
        edad = Teclado.Teclado.read_integer(f"Ingrese la edad de {nombre}:", min_value=0)
        personas.append((nombre, edad))

    print("Lista original de personas:")
    for p in personas:
        print(p)

    # Ordena por edad
    personas_ordenadas = BubbleSort.bubble_sort(personas.copy(), key=lambda x: x[1])
    print("\nPersonas ordenadas por edad (ascendente):")
    for p in personas_ordenadas:
        print(p)


def ejemplo_descendente():
    # Ordena descendente enteros
    cantidad = Teclado.Teclado.read_integer("¿Cuántos números enteros deseas ordenar en forma descendente?", min_value=1)
    lista = []
    for i in range(cantidad):
        numero = Teclado.Teclado.read_integer(f"Ingrese el número entero #{i + 1}:")
        lista.append(numero)

    print("Lista original:", lista)
    # Ordena en reversa
    lista_ordenada = BubbleSort.bubble_sort(lista.copy(), reverse=True)
    print("Lista ordenada (descendente):", lista_ordenada)


def main():
    # Menú principal ejemplos
    while True:
        print("\n----- Menú de Ejemplos de Bubble Sort -----") # Muestra las opciones
        print("1. Ordenar lista de enteros (ascendente)")
        print("2. Ordenar lista de flotantes (ascendente)")
        print("3. Ordenar lista de textos (alfabéticamente)")
        print("4. Ordenar lista de personas (por edad ascendente)")
        print("5. Ordenar lista de enteros (descendente)")
        print("6. Salir")
        opcion = Teclado.Teclado.read_integer("Seleccione una opción (1-6):", min_value=1, max_value=6) # Lee la opción

        if opcion == 1:
            ejemplo_enteros() # Llama ejemplo enteros
        elif opcion == 2:
            ejemplo_flotantes() # Llama ejemplo flotantes
        elif opcion == 3:
            ejemplo_textos() # Llama ejemplo textos
        elif opcion == 4:
            ejemplo_personas() # Llama ejemplo personas
        elif opcion == 5:
            ejemplo_descendente() # Llama ejemplo descendente
        elif opcion == 6:
            print("Saliendo...") # Indica salida
            break

        input("\nPresione Enter para continuar...") # Pausa para continuar


if __name__ == '__main__':
    main() # Inicia la aplicación