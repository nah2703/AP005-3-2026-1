'''
Los diccionarios  son estructuras de datos mutables y desordenadas 
que almacenan pares clave:valor entre llaves {}, permitiendo un acceso 
rápido y eficiente a los datos. Son dinámicos, lo que significa que pueden 
crecer o decrecer, y sus claves deben ser inmutables (como cadenas, números 
o tuplas).
'''

sensores = {"Sala": 21, "Cocina":23, "Habitacion": 20, "Despensa": 22}
numCamaras = {"Patio": 6, "Garaje": 2, "Porton": 1}
print(sensores)
print(numCamaras)
print(type(sensores))

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
print(translations)
potencias = {2:[1, 2, 4, 8, 16], 3:[1, 3, 9, 27, 81]}
print(potencias)

hijos = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(hijos)

diccionarioVacio = {}
print(diccionarioVacio)



menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2} 
print("Before: ", menu) 
menu["cheesecake"] = 8 
print("After", menu)
animals_in_zoo = {"dinosaurs": 0} 
animals_in_zoo = {"dinosaurs": 0} 
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)

sensores = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensores)

sensores.update({"Patio": 6, "Garaje": 2, "Porton": 1}) 
print("After: ", sensores)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

menu["banana"] = 3
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5 
menu["chocolate"] = 6
print("After:", menu) 

print("##################################")

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
oscar_winners.update({"Supporting Actress": "Viola Davis"}) 
print("After1", oscar_winners)
print()
oscar_winners["Best Picture"] = "Moonlight" 
print("After2", oscar_winners)
nombres = ['Jenny', 'Alexus', 'Sam', 'Grace']
alturas = [61, 70, 67, 64]

zipEstudiantes = zip(nombres, alturas)
print(type(zipEstudiantes))
print(zipEstudiantes)

estudiantes = {key:value for key, value in zipEstudiantes}
print(estudiantes)

bebidas = ["espresso", "chai", "decaf", "drip"]
cafeina = [64, 40, 0, 120]

combinacionBebidasCafeina = zip(bebidas, cafeina)
print(combinacionBebidasCafeina)

cafeinaenBebidas = {key:value for key, value in combinacionBebidasCafeina}
print(cafeinaenBebidas)
print()
print()
print()
print("###########################")
print()
print()
print()
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("After: ", plays)
library = {"The Best Songs": plays, "Sunday Feelings": {}}