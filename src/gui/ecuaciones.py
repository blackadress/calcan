## CONSTANTES
ROUND_DIGITS = 5
GRAVITY = 9.80665
GRAVITY_ENG = 32.17404856

## COMUN
# F
def numero_de_froude(v, A, T, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = v / (gravity * A / T)**(1/2)
    return round(res, ROUND_DIGITS)

# S
def pendiente_critica(Q, n, A, R, SI=True):
    res = ((Q * n) / (A * R**(2/3)))**(1/2)
    return round(res, ROUND_DIGITS)


## TRIANGULAR
# y
def tirante_critico_triangular(Q, z, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = ((2 * Q**2) / (gravity * z**2))**(1/5)
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_triangular(y, z, SI=True):
    res = (z * y**2)
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_triangular(y, z, SI=True):
    res = 2 * z * y
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_triangular(y, z, SI=True):
    res = 2 * y * (1 + z**2)**(1/2)
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_triangular(A, P, SI=True):
    res = A / P
    return round(res, ROUND_DIGITS)

# v
def velocidad_triangular(y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = ((gravity * y) / 2)**(1/2)
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_triangular(y, v, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = y + (v**2) / (2 * gravity)
    return round(res, ROUND_DIGITS)


## RECTANGULAR
# y
def tirante_critico_rectangular(Q, b, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = ((Q**2) / (gravity * b**2))**(1/3)
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_rectangular(b, y, SI=True):
    res = (b * y)
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_rectangular(b, SI=True):
    res = b
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_rectangular(b, y, SI=True):
    res = b + 2 * y
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_rectangular(b, y, SI=True):
    res = (b * y) / (b + 2 * y)
    return round(res, ROUND_DIGITS)

# v
def velocidad_rectangular(y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = (gravity * y)**(1/2)
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_rectangular(y, v, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = y + (v**2) / (2 * gravity)
    return round(res, ROUND_DIGITS)


## TRAPEZOIDAL
# y
def tirante_critico_trapezoidal(Q, b, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_trapezoidal(b, y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_trapezoidal(b, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_trapezoidal(b, y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_trapezoidal(b, y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# v
def velocidad_trapezoidal(y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_trapezoidal(y, v, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)


## TRAPEZOIDAL
# y
def tirante_critico_circular(Q, b, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_circular(b, y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_circular(b, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_circular(b, y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_circular(b, y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# v
def velocidad_circular(y, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_circular(y, v, SI=True):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = 0
    return round(res, ROUND_DIGITS)

