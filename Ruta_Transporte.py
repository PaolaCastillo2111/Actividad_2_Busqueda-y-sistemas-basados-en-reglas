# S.I rutas de transporte

from queue import PriorityQueue

# =======================================
# GRAFO DEL SISTEMA DE TRANSPORTE BOGOTA
# =======================================

grafo = {

    "Portal Norte": {"Portal Suba": 7,"Portal El Dorado": 10},
    "Portal Suba": {"Portal Norte": 7,"Portal 80": 5,"Ricaurte": 8},
    "Portal 80": {"Portal Suba": 5,"Ricaurte": 6},
    "Ricaurte": {"Portal 80": 6,"Portal Americas": 4,"Portal Sur": 7,"Portal El Dorado": 5},
    "Portal Americas": {"Ricaurte": 4},
    "Portal Sur": {"Ricaurte": 7,"Portal Tunal": 5,"Portal San Mateo": 6},
    "Portal Tunal": {"Portal Sur": 5,"Portal 20 De Julio": 3,"Portal Usme": 4},
    "Portal 20 De Julio": {"Portal Tunal": 3},
    "Portal Usme": {"Portal Tunal": 4},
    "Portal El Dorado": {"Portal Norte": 10,"Ricaurte": 5},
    "Portal San Mateo": {"Portal Sur": 6}
}

# ====================================
# HEURÍSTICA (estimación al destino)
# ====================================

heuristica = {

    "Portal Norte": 15,
    "Portal Suba": 12,
    "Portal 80": 10,
    "Ricaurte": 7,
    "Portal Americas": 8,
    "Portal Sur": 4,
    "Portal Tunal": 3,
    "Portal 20 De Julio": 2,
    "Portal Usme": 1,
    "Portal El Dorado": 9,
    "Portal San Mateo": 0
}

# ====================================
# ALGORITMO A*
# ====================================

def algoritmo_a_estrella(grafo, inicio, destino):

    cola_prioridad = PriorityQueue()

    cola_prioridad.put((0, inicio))

    caminos = {}

    costo_acumulado = {}

    caminos[inicio] = None
    costo_acumulado[inicio] = 0

    while not cola_prioridad.empty():

        nodo_actual = cola_prioridad.get()[1]

        # Verificar destino
        if nodo_actual == destino:
            break

        # Revisar vecinos
        for vecino in grafo[nodo_actual]:

            nuevo_costo = (
                costo_acumulado[nodo_actual]
                + grafo[nodo_actual][vecino]
            )

            # Verificar mejor camino
            if (
                vecino not in costo_acumulado
                or nuevo_costo < costo_acumulado[vecino]
            ):

                costo_acumulado[vecino] = nuevo_costo

                prioridad = (
                    nuevo_costo
                    + heuristica[vecino]
                )

                cola_prioridad.put((prioridad, vecino))

                caminos[vecino] = nodo_actual

    # Reconstrucción de ruta
    ruta = []

    nodo = destino

    while nodo is not None:

        ruta.append(nodo)

        nodo = caminos[nodo]

    ruta.reverse()

    return ruta

# Programa mejor ruta

print("=== S.I RUTA DE TRANSMILENIO BOGOTA ===")

inicio = input("Ingrese estación inicial: ").title()

destino = input("Ingrese estación destino: ").title()

# Validar estaciones
if inicio not in grafo or destino not in grafo:

    print("Uno de los portales no existe en el sistema.")

else:

    resultado = algoritmo_a_estrella(grafo,inicio,destino)
    
# Mostrar resultado
    print("Esta es la mejor ruta encontrada es:")

    for estacion in resultado:

        print(estacion)
