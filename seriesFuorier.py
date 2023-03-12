from matplotlib.pyplot import *
from numpy import *
from os import system

# Se define una función llamada "serieFuorierTriangular" que toma como argumentos un arreglo "x" 
# y un entero "iteraciones", la función calcula y devuelve la serie de Fourier de la señal
# triangular.
def serieFuorierTriangular(x, iteraciones):
    suma = 0
    for i in range(iteraciones):
        suma += ((sin((2*i-1)*x)) * (((-1)**i) / ((2*i-1)**2)))
    return suma

def serieFuorierCuadrada(x, iteraciones):
    suma = 0
    for i in range(iteraciones):
        suma += ((sin((2*i+1)*x)) / (2*i+1))
    return suma

def serieFuorierDientesSierra(x, iteraciones):
    suma = 0
    for i in range(iteraciones):
        suma += (sin((i+1)*x) / (i+1))
    return suma

while(1):
    # Se hace uso de la función system para limpiar la consola
    system("clear")
    print("\n1.- Señal Cuadrada")
    print("2.- Señal Triangular")
    print("3.- Señal Dientes de Sierra")
    print("4.- Salir")
    opc = int(input("Introduzca una opcion: "))
    if (opc == 1):
        # Se hace uso de la función system para limpiar la consola
        system("clear")
        # Solicita al usuario el rango mínimo para graficar la función.
        rangoMin = int(input("\nIntroduzca el rango minimo: "))
        # Solicita al usuario el rango máximo para graficar la función
        rangoMax = int(input("Introduzca el rango máximo: "))
        # Solicita al usuario el número de iteraciones a utilizar en la serie de Fourier.
        iteraciones = int(input("Introduzca el numero de iteraciones: "))

        # Crea un arreglo de 1000 puntos equidistantes entre el rango mínimo y el rango máximo ambos
        # multiplicados por PI e introducidos por el usuario, la función "linspace" 
        # genera un arreglo que cubre el rango completo de la señal, desde "rangoMin" hasta 
        # "rangoMax" veces pi.
        x = linspace(rangoMin * pi, rangoMax * pi, 1000)

        # Se grafica la serie de Fourier utilizando la función plot de Matplotlib.
        # Utilizamos el arreglo x y la función serieFuorierCuadrada para obtener los 
        # valores de la señal.
        # 'g-' indica que la línea debe ser de color verde.
        plot(x, serieFuorierCuadrada(x, iteraciones), 'g-')
        # Se configura la etiqueta del eje x
        xlabel("Tiempo")
        # Se configura la etiqueta del eje y
        ylabel("Amplitud")
        # Se configura el titulo de la grafica
        title("Serie de Fuorier para una señal cuadrada")
        # Se configura la leyenda de la grafica
        legend(['Señal Cuadrada'])
        # Se muestra la grafica
        show()
    elif (opc == 2):
        # Se hace uso de la función system para limpiar la consola
        system("clear")
        # Solicita al usuario el rango mínimo para graficar la función.
        rangoMin = int(input("Introduzca el rango minimo: "))
        # Solicita al usuario el rango máximo para graficar la función
        rangoMax = int(input("Introduzca el rango máximo: "))
        # Solicita al usuario el número de iteraciones a utilizar en la serie de Fourier.
        iteraciones = int(input("Introduzca el numero de iteraciones: "))

        # Crea un arreglo de 1000 puntos equidistantes entre el rango mínimo y el rango máximo ambos
        # multiplicados por PI e introducidos por el usuario, la función "linspace" 
        # genera un arreglo que cubre el rango completo de la señal, desde "rangoMin" hasta 
        # "rangoMax" veces pi.
        x = linspace(rangoMin * pi, rangoMax * pi, 1000)

        # Se grafica la serie de Fourier utilizando la función plot de Matplotlib.
        # Utilizamos el arreglo x y la función serieFuorierTriangular para obtener 
        # los valores de la señal.
        # 'g-' indica que la línea debe ser de color verde.
        plot(x, serieFuorierTriangular(x, iteraciones), 'g-')
        # Se configura la etiqueta del eje x
        xlabel("Tiempo")
        # Se configura la etiqueta del eje y
        ylabel("Amplitud")
        # Se configura el titulo de la grafica
        title("Serie de Fuorier para una señal cuadrada")
        # Se configura la leyenda de la grafica
        legend(['Señal Cuadrada'])
        # Se muestra la grafica
        show()
    elif (opc == 3):
        # Se hace uso de la función system para limpiar la consola
        system("clear")
        # Solicita al usuario el rango mínimo para graficar la función.
        rangoMin = int(input("Introduzca el rango minimo: "))
        # Solicita al usuario el rango máximo para graficar la función
        rangoMax = int(input("Introduzca el rango máximo: "))
        # Solicita al usuario el número de iteraciones a utilizar en la serie de Fourier.
        iteraciones = int(input("Introduzca el numero de iteraciones: "))

        # Crea un arreglo de 1000 puntos equidistantes entre el rango mínimo y el rango máximo ambos
        # multiplicados por PI e introducidos por el usuario, la función "linspace" 
        # genera un arreglo que cubre el rango completo de la señal, desde "rangoMin" hasta 
        # "rangoMax" veces pi.
        x = linspace(rangoMin * pi, rangoMax * pi, 1000)

        # Se grafica la serie de Fourier utilizando la función plot de Matplotlib.
        # Utilizamos el arreglo x y la función serieFuorierDientesSierra para obtener 
        # los valores de la señal.
        # 'g-' indica que la línea debe ser de color verde.
        plot(x, serieFuorierDientesSierra(x, iteraciones), 'g-')
        # Se configura la etiqueta del eje x
        xlabel("Tiempo")
        # Se configura la etiqueta del eje y
        ylabel("Amplitud")
        # Se configura el titulo de la grafica
        title("Serie de Fuorier para una señal dientes de sierra")
        # Se configura la leyenda de la grafica
        legend(['Señal Dientes de Sierra'])
        # Se muestra la grafica
        show()
    elif (opc == 4):
        # Se hace uso de la función system para limpiar la consola
        system("clear")
        exit()