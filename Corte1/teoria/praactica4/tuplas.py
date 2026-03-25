'''
Las listas en Python son estructuras de datos ordenadas, mutables y
versátiles, definidas mediante corchetes [] para almacenar conjuntos 
arbitrarios de elementos (números, textos, o mezcla de tipos). Son fundamentales
por su dinamismo, permitiendo añadir (append), eliminar (pop, remove) y modificar
elementos, usando índices que comienzan en 0.
Características Principales:
-Ordenadas: Mantienen el orden de inserción.
-Mutables: Se pueden cambiar, añadir o eliminar elementos.
-Indexables: Acceso por índice, ej. lista[0] es el primer elemento.
-Heterogéneas: Pueden contener distintos tipos de datos simultáneamente.
'''

miLista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] 
print(miLista) 
print(type(miLista)) 

print(miLista[2]) 
print("Longitud de miLista: ", len(miLista)) 
print(miLista[0:2]) 
print(miLista[:2]) 

miLista.append('Blanco') 
print(miLista)
miLista.insert(3, 'Negro') 
print(miLista)
miLista.extend(['Marron', 'Gris']) 
print(miLista)
print(miLista.index('Azul')) 
miLista.remove('Marron') 
print(miLista)
miLista.insert(8, 'Marron')
print(miLista)
print("Instruccion .pop")
print(miLista.pop()) 
print("Longitud miLista: ", len(miLista))
miLista3 = miLista*3 
print("miLista3: ", miLista3)
print("Instruccion .sort")
miListaOrdenada = miLista.sort() 
print(miListaOrdenada)
print(miLista)

miListaNum = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordenando lista numeros.")
miListaNum.sort()
print(miListaNum)

miListaNum.sort(reverse=True) 
print("De mayor a menor: ", miListaNum)

'''
Las tuplas son  estructuras de datos ordenadas e inmutables (no se 
pueden modificar, añadir o eliminar elementos tras su creación). Se 
definen mediante paréntesis () y comas, siendo ideales para agrupar 
datos relacionados que no deben cambiar, como coordenadas o registros, 
ofreciendo mayor seguridad y rendimiento.
'''
miTupla = tuple(miLista) 
print("miTupla: ", miTupla)
print(miTupla[0]) 
print(miTupla[2])


print('Rojo' in miTupla) 
print(miTupla.count('Rojo')) 

miTuplaUnitaria = ('Blanco')
print(miTuplaUnitaria)


miTuplaDos = 'Gaspar', 4, 5, 1999
print(miTuplaDos)