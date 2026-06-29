   
def nombre_valido(nombre):
    if len(nombre) >= 3 and nombre.isalpha():
        devolver = True
    else:
        devolver = False
    return devolver

def crear_codename(nombre, nivel):
    a = nombre[0:3].upper()+ "-Lv" + str(nivel)
    return a

def vida_maxima(nivel):
    return 100 + (nivel ** 2) * 5

# ===== PARTE B ===== 
def clasificar_arma(opcion_menu):
    if opcion_menu == 1:
        return "Legendaria"
    elif opcion_menu == 2:
        return "Media"
    else:
        return "Debil"

def es_critico(es_magica, nivel):
    return es_magica or nivel >= 10

def dano_base(ataque, poder, defensa):
    return (ataque + poder) - defensa

def dano_total(ataque, poder, defensa, critico):
    base = dano_base(ataque, poder, defensa)
    if critico == True:
        return base * 2
    else:
        return base

# ===== PARTE C =====
def porcentaje_vida(actual, maxima):
    porc= actual / maxima *100
    return porc
def estado_vida(porc):
    if porc<=20:
        return "critico"
    elif porc<= 40:
        return "herido"
    else:
        return "Sano"
def comprar_pociones(monedas, precio):
    cantidad= monedas//precio
    vuelto= monedas%precio
    return cantidad, vuelto

# ===== PARTE D =====
def puede_atacar(energia, esta_aturdido):
    if energia > 0 and not esta_aturdido== False:
        return True
    else:
        return False
def vida_restante(vida, dano):
    vidares= vida - dano
    return vidares
def gana(vida_heroe, vida_enemigo):
    if vida_heroe > vida_enemigo:
        return True
    else:
        return False




nombre=input("dame tu nombre:") 
arma=input("ingresa tu arma")
print("Nombre valido", nombre_valido(nombre))
print("Codename",crear_codename(nombre, 100))
print("Vida maxima",vida_maxima(10))
print("1 - escopeta")
print("2 - espada")
print("3 - tirachinas")

opcion = int(input("Escriba el numero de su arma: "))

if opcion == 1:
    es_magica = True
else:
    es_magica = False

nivel = 0

if opcion == 1:
    poder = 50  
elif opcion == 2:
    poder = 25  
else:
    poder = 5    

ataque = 40      
defensa = 15

resultado_arma = clasificar_arma(opcion)
resultado_critico = es_critico(es_magica, nivel)
danio_base_calculado = dano_base(ataque, poder, defensa)
danio_final = dano_total(ataque, poder, defensa, resultado_critico)

print("El poder de tu arma es:", resultado_arma)
print("¿El golpe es crítico?:", resultado_critico)
print("El daño BASE realizado es:", danio_base_calculado)
print("El daño total realizado es:", danio_final)
print(porcentaje_vida(100, 1000))
print(estado_vida(20))
print(comprar_pociones(100, 80))
print(puede_atacar(3, False))
print(vida_restante(10, 8))
print(gana(2, 9))
