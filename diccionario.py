#diccionario
# coleccion de datos que 
# los almacena en pares
#clave_valor
#-cada clave es un string
#- el valor puede ser de cualqueir tipo
#- un diccionario comienza y termina
#con llaves (curly braces)
#- la clave se separa del valor por dos puntos(:)
#- cada elemento (propiedad) del 
# diccionario se separa por una coma


# ejemplo: diccionario
# que almacene un pais
pais1 ={
    "nombre" : "colombia",
    "capital" : "Bogota",
    "moneda" : "pesos",
    "ciudades" :[
        "cordoba",
        "choco",
        "cali",
        "medellin"
    ],
    "poblacion" : {
                    "censo" : 53,
                    "densidad" : 46
                    }
 }
pais2 = {
    "nombre" : "ecuador",
    "capital" : "quito",
    "moneda" : "dolar",
    "ciudades": [   
        "azogues",
        "macas",
        "portoviejo",

    ],
    "poblacion" : {
                    "censo" : 18,
                    "densidad" : 64
                    }
}

pais3 = {
    "nombre" : "brasil",
    "capital" : "brasilia",
    "moneda" : "real",
    "ciudades": [   
        "rio de janeiro",
        "sao paublo",
        "manaos",

    ]
    ,
    "poblacion" : {
                    "censo" : 203,
                    "densidad" : 205
                    }

}

#aceder a la informacion del pais 
print(pais1["nombre"])
print(pais2["capital"])
print(pais3["ciudades"][2])

print("-------------------------")
for ciudad in pais1["capital"]:
    print(ciudad)

##acceder a datoss poblacionales 
print("----------------------")

print("censo",pais1["poblacion"]
      ["censo"], 
      "millones de habitantes")
print("densidad",pais1["poblacion"]
      ["densidad"], 
      "por km2")






