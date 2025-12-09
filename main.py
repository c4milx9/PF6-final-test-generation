import requests

#Saludo
print("Hola buen día, bienvenidos a Colombia platos típicos")
#Preguntar que desean ordenar
print("Aquí les tengo el menú de los platos típicos de Colombia ¿Qué van a comer el día de hoy?\n")

#Consultar los platos típicos
url = "https://api-colombia.com/api/v1/TypicalDish"
respuesta = requests.get(url)
platos = respuesta.json()

#Mostrar el menu
print("----- MENÚ DE PLATOS TÍPICOS -----\n")
for plato in platos:
    nombre = plato.get("name")
    departamento = plato.get("department", {}).get("name", "Departamento no disponible")
    print(f"- {nombre} del departamento de {departamento}")

#Preguntar al cliente el plato
eleccion = input("\n¿Qué plato desean pedir hoy?: ").strip().lower()

print("\nBuscando su plato...\n")

#Buscar el plato elegido
encontrado = False
for plato in platos:
    if plato.get("name", "").lower() == eleccion:
        encontrado = True
        print(f"Aqui esta su plato: {plato.get('name')}")
        print(f"Descripción: {plato.get('description')}")
        print("\n¡Provecho, que lo disfrute!\n")
        break

if not encontrado:
    print("Lo siento, no encontramos ese plato en nuestro menú.")


