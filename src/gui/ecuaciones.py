## CONSTANTES
ROUND_DIGITS = 4
GRAVITY = 9.81

## COMUN

# F
def numero_de_froude(v, A, T):
    res = v / (GRAVITY * A / T)**(1/2)
    return round(res, ROUND_DIGITS)

# S
def pendiente_critica(Q, n, A, R):
    res = ((Q * n) / (A * R**(2/3)))**(1/2)
    return round(res, ROUND_DIGITS)


## TRIANGULAR

# y
def tirante_critico_triangular(Q, z):
    res = ((2 * Q**2) / (GRAVITY * z**2))**(1/5)
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_triangular(y, z):
    res = (z * y**2)
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_triangular(y, z):
    res = 2 * z * y
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_triangular(y, z):
    res = 2 * y * (1 + z**2)**(1/2)
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_triangular(y, z):
    res = z * y / (2 * (1 + z**2)**(1/2))
    return round(res, ROUND_DIGITS)

# v
def velocidad_triangular(y):
    res = ((GRAVITY * y) / 2)**(1/2)
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_triangular(y, v):
    res = y + (v**2) / (2 * GRAVITY)
    return round(res, ROUND_DIGITS)



## RECTANGULAR
# y
def tirante_critico_rectangular(Q, b):
    res = ((Q**2) / (GRAVITY * b**2))**(1/3)
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_rectangular(b, y):
    res = (b * y)
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_rectangular(b):
    res = b
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_rectangular(b, y):
    res = b + 2 * y
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_rectangular(b, y):
    res = (b * y) / (b + 2 * y)
    return round(res, ROUND_DIGITS)

# v
def velocidad_rectangular(y):
    res = (GRAVITY * y)**(1/2)
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_rectangular(y, v):
    res = y + (v**2) / (2 * GRAVITY)
    return round(res, ROUND_DIGITS)


## TRAPEZOIDAL
# y
def tirante_critico_trapezoidal(Q, b):
    res = 0
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_trapezoidal(b, y):
    res = 0
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_trapezoidal(b):
    res = 0
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_trapezoidal(b, y):
    res = 0
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_trapezoidal(b, y):
    res = 0
    return round(res, ROUND_DIGITS)

# v
def velocidad_trapezoidal(y):
    res = 0
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_trapezoidal(y, v):
    res = 0
    return round(res, ROUND_DIGITS)


## TRAPEZOIDAL
# y
def tirante_critico_circular(Q, b):
    res = 0
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_circular(b, y):
    res = 0
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_circular(b):
    res = 0
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_circular(b, y):
    res = 0
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_circular(b, y):
    res = 0
    return round(res, ROUND_DIGITS)

# v
def velocidad_circular(y):
    res = 0
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_circular(y, v):
    res = 0
    return round(res, ROUND_DIGITS)


