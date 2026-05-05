from aircraft import Aircraft

modelo = input("Enter aircraft model: ")
mi_avion = Aircraft(modelo)

while True:
    comando_usuario = input("Enter command (A for ascent, D for descent, X to exit): ")
    
    if comando_usuario.upper() == 'X':
        break
    
    partes = comando_usuario.split()
    
    if len(partes) == 2:
        accion = partes[0].upper()
        pies = int(partes[1])
        
        if accion == 'A':
            mi_avion.climb(pies)
        elif accion == 'D':
            mi_avion.descend(pies)

print(f"Final altitude: {mi_avion.altitude} feet")