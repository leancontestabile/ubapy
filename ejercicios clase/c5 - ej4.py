#Ejercicio ciclos anidados.
#Se tienen 10 cursos de 30 alumnos de los cuales se quiere saber lo siguiente:
#El promedio de cada curso
#El curso que mayor promedio tiene
#El nombre del alumno que mayor nota obtuvo (se supone único) y a que curso pertenece

sumanotas = 0
promediomax = 0
notamax = 0

for cursos in range(10):
    for alumnos in range(30):
        alumno : str = str(input("ingrese su nombre: "))
        nota : int = int(input("ingrese la nota: "))
        
        sumanotas : int = (sumanotas + nota)
    
        if (nota > notamax):
           notamax = nota
           nnotamax = alumno
           cursomax = cursos
    
    promedio : int = (sumanotas / 30)

    if (promedio > promediomax):
            promediomax = promedio
            npromediomax = cursos

    print("el promedio del curso", cursos, "es", promedio)

    sumanotas = 0
    
print("el mayor promedio es el curso:", npromediomax)
print("la mayor nota es", notamax, "de", nnotamax, "del curso", cursomax)