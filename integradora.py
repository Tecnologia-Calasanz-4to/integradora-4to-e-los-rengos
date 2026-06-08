nombre=input("dame tu nombre:")
arma=input("ingresa tu arma")
def nombre_valido(nombre):
    if nombre >= 3 and nombre.isalpha:
        return(nombre)
def crear_codename(nombre, nivel):
    
return    # TODO: nombre[0:3].upper() + "-Lv" + str(nivel)
def vida_maxima(nivel):
    pass    # TODO: 100 + nivel ** 2 * 5

# ===== PARTE B =====
arma=input("ingresa un arma")
print(arma)
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
    pass    # TODO: actual / maxima * 100
def estado_vida(porcentaje):
    pass    # TODO: if/elif/else -> "CRITICO"/"HERIDO"/"SANO"
def comprar_pociones(monedas, precio):
    pass    # TODO: monedas // precio  y  monedas % precio

# ===== PARTE D =====
def puede_atacar(energia, esta_aturdido):
    pass    # TODO: energia > 0 and not esta_aturdido
def vida_restante(vida, dano):
    pass    # TODO: si vida - dano < 0 -> 0 ; si no -> vida - dano
def gana(vida_heroe, vida_enemigo):
    pass    # TODO: vida_heroe > 0 and vida_enemigo <= 0
