   
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
def clasificar_arma(poder):
    return    # TODO: if/elif/else -> "Legendaria"/"Media"/"Debil"
def es_critico(es_magica, nivel):
    pass    # TODO: es_magica or nivel >= 10
def dano_base(ataque, poder, defensa):
    pass    # TODO: (ataque + poder) - defensa
def dano_total(ataque, poder, defensa, critico):
    pass    # TODO: si critico -> dano_base(...) * 2 ; si no -> dano_base(...)

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
    pass    # TODO: energia > 0 and not esta_aturdido
def vida_restante(vida, dano):
    pass    # TODO: si vida - dano < 0 -> 0 ; si no -> vida - dano
def gana(vida_heroe, vida_enemigo):
    pass    # TODO: vida_heroe > 0 and vida_enemigo <= 0




nombre=input("dame tu nombre:") 
arma=input("ingresa tu arma")
print("Nombre valido", nombre_valido(nombre))
print("Codename",crear_codename(nombre, 100))
print("Vida maxima",vida_maxima(10))
print(porcentaje_vida(100, 1000))
print(estado_vida(20))
print(comprar_pociones(100, 80))
