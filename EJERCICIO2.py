#----                   ------
#---- PUNTO 1º,2º,3º,4º ------
#----                   ------

nombre_sistema = "Catalogo de Piezas"
precio_pieza = "25"
categoria = "cartas"
estatus = "disponible"
descripcion = "Cartas variadas"
print("\n", nombre_sistema, precio_pieza, categoria, estatus, descripcion)

precio_pieza = float(precio_pieza)
print("\nVariables:", nombre_sistema, type(nombre_sistema)), print(precio_pieza, type(precio_pieza)), print(categoria, type(categoria)), print(estatus, type(estatus)), print(descripcion, type(descripcion))

#-----        ------
#-----PUNTO 5º------
#-----        ------

precio_pieza = str(precio_pieza)

#concatenación
mensaje1 = "sistema " + nombre_sistema + " precio " + precio_pieza + " categoria " + categoria + " estatus " + estatus + " descripcion " + descripcion
print("\nConcatenación:", mensaje1)

#interpolación
mensaje2 = f"sistema: {nombre_sistema} precio: {precio_pieza} categoria: {categoria} estatus: {estatus} descripcion: {descripcion}"
print("Interpolación:", mensaje2)

#separación por comas
print("Separación por comas:", nombre_sistema, precio_pieza, categoria, estatus, descripcion)

#split
etiquetas = "retro, anime, limited, vintage, rare "
print("Split:", etiquetas)


#Replace
descripcion = "Figura usada con algunos detalles"
descripcion_actualizada = descripcion.replace("usada", "certificada")
print("Replace:", descripcion_actualizada)


#lower / upper / title
print("\nsistema:", nombre_sistema)
print("lower:", nombre_sistema.strip().lower())
print("upper:", nombre_sistema.strip().upper())
print("tittle:", nombre_sistema.strip().title())


#-----        ------
#-----PUNTO 6º------
#-----        ------

#Ver elementos de la lista (he transformado la variable etiquetas del ejercicio anterior)
lista_etiquetas = etiquetas.split(", ")
print("\nlista:", lista_etiquetas)

#Añadir elemento a la lista
lista_etiquetas.append("coleccion ")
print("elemento añadido:", lista_etiquetas)
print("selección de elemento:", lista_etiquetas[2])

#Eliminar elemento
lista_etiquetas.remove("vintage")
print("elemento borrado:", lista_etiquetas)

#Actualizar un elemento
lista_etiquetas[2] = "edicion_limitada"
print("lista actualizada:",lista_etiquetas)



#-----        ------
#-----PUNTO 7º------
#-----        ------


#OPERADORES COMPARATIVOS
total_etiquetas = len(lista_etiquetas)
print("\n¿la lista tiene más de 3 elementos?:", total_etiquetas >3)
print("¿la lista tiene menos de 3 elementos?:", total_etiquetas <3)


#OPERADORES LÓGICOS
favoritos = ("retro" in lista_etiquetas) and ("anime" in lista_etiquetas)
print("\n¿están en favoritos?:", favoritos)

combos = ("limited" in lista_etiquetas) or ("rare" in lista_etiquetas)
print("¿están en combos alguno de los dos?:", combos)


#OPERADOREES ARITMÉTICOS
nuevas_etiquetas = ["pokemon ", "digimon"]
lista_completa = lista_etiquetas + nuevas_etiquetas
print("\nlista completa:", lista_completa)


#-----        ------
#-----PUNTO 8º------
#-----        ------


#CONDICIONALES
if combos:
    print("\n¡Genial! Tienes un combo muy buscado en tu lista.")
else:
    print("\nNo tienes ningún combo súper buscado en la lista.")


if len(lista_etiquetas) <3:
    print("\nMuy bien.")
else:
    print("\nAñade más etiquetas.")



#-----                            ------
#-----FUNCIONES (encapsular y reutilizar)------
#-----                            ------

#función para mostrar la ficha de una pieza
def mostrar_pieza(nombre_sistema_mostrar, categoria_mostrar, precio_mostrar, estatus_mostrar, descripcion_mostrar):
    print(f"nombre: {nombre_sistema_mostrar} categoria: {categoria_mostrar} precio: {precio_mostrar} estatus: {estatus_mostrar} descripcion: {descripcion_mostrar}")

#función con validación temprana: el precio debe ser número y mayor que cero
def validar_precio(valor):
    try:
        numero = float(valor)
    except ValueError:
        return False
    if numero > 0:
        return True
    else:
        return False

#función con validación temprana: la descripción debe tener usada o certificada
def validar_descripcion(texto):
    if "usada" in texto.lower() or "certificada" in texto.lower():
        return True
    else:
        return False


#-----        ------
#-----PUNTO 9º------
#-----        ------


#BLUCLES
print("\n--- Lista completa de mis etiquetas favoritas ---")

for etiqueta in lista_completa:
    print(f"- {etiqueta}")

print("\n--- Ficha de la pieza ---")
mostrar_pieza(nombre_sistema, categoria, precio_pieza, estatus, descripcion)

print("\n--- Validacion temprana de la pieza ---")
if validar_precio(precio_pieza):
    print("El precio es valido.")
else:
    print("⚠️ Error: el precio no es un numero mayor que cero.")

if validar_descripcion(descripcion):
    print("La descripcion es valida.")
else:
    print("⚠️ Error: la descripcion debe contener 'usada' o 'certificada'.")



#-----         ------
#-----PUNTO 10º------
#-----         ------




#VALIDACIÓN DE DATOS POR EL USUARIO
busqueda = input("Introduce el nombre de la etiqueta: ")

busqueda_limpia = busqueda.lower()

etiquetas_minusculas = [etiqueta.lower() for etiqueta in lista_etiquetas]

if busqueda_limpia == "":
    print("⚠️ Error: No puedes dejar el campo vacío. Debes introducir una etiqueta.")

elif busqueda_limpia in etiquetas_minusculas:
    print(f"🎉 ¡CORRECTO! '{busqueda}' es una etiqueta.")

else:
    print(f"❌ ERROR: '{busqueda}' no es una etiqueta.")


#CAPTURA DE ERRORES CON TRY / EXCEPT
entrada = input("\nIntroduce un precio para convertir a numero: ")

try:
    entrada_numero = float(entrada)
    print(f"Precio convertido: {entrada_numero}")

except ValueError:
    print(f"❌ Error: '{entrada}' no es un numero. No se puede convertir.")
