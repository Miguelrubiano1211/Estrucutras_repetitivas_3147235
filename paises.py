paises = [
            {
                "nombre":"venezuela",
                "capital":"caracas",
                "pesos":"bolivar",
                "poblacion":
                    {
                        "censo": 26,
                        "densidad":28
                    },
                "ciudades" :[
                                "caracas",
                                "martacaibo",
                                "san cristobal",
                                "cumana"
                            ],
                "superficie" :{
                                "total":916 
                            }
            },
            {
                "nombre":"colombia",
                "capital":"Bogota",
                "pesos":"pesos colombianos",
                "poblacion":
                    {
                        "censo": 53,
                        "densidad": 46
                    },
                "ciudades" :[
                                "bogota",
                                "medellin",
                                "cali",
                                "barranquilla"
                            ],
                "superficie" :{
                                "total":1.141
                            },
            },
            {
                "nombre":"brasil",
                "capital":"brasilia",
                "pesos":"real",
                "poblacion":
                    {
                        "censo":203,
                        "densidad":205
                    },
                "ciudades" :[
                                "rio de janeiro",
                                "sao paublo",
                                "manaos",
                                "Natai"
                            ],
                "superficie" :{
                                "total":8.515                     
                            },
            },
        ]
# recorrer todos los paises:
print("Recorriendo todos los paises")
for pais in paises:
    print("nombre:", pais["nombre"])
    print("-------------------------")
    print("capital:",pais["capital"])
    print("-------------------------")
    print("superficie:",pais["superficie"]["total"])
    print("-------------------------")
    print("poblacion:")
    print("censo:",pais["poblacion"]["censo"],"millones")
    print("densidad:",pais["poblacion"]["densidad"],"por km2")
    print("-------------------------")
    print("ciudades principales:")
    for ciudad in pais["ciudades"]:
            print("-", ciudad)


