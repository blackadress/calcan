import math

## CONSTANTES
ROUND_DIGITS = 5
GRAVITY = 9.80665
GRAVITY_ENG = 32.17404856
ERROR = 0.00001

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
def pendiente_critica(Q, n, A, R, SI):
    res = ((Q * n) / (A * R**(2/3)))**(1/2)
    return round(res, ROUND_DIGITS)


## TRIANGULAR
# y
def tirante_critico_triangular(Q, z, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = ((2 * Q**2) / (gravity * z**2))**(1/5)
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_triangular(y, z, SI):
    res = (z * y**2)
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_triangular(y, z, SI):
    res = 2 * z * y
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_triangular(y, z, SI):
    res = 2 * y * (1 + z**2)**(1/2)
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_triangular(A, P, SI):
    res = A / P
    return round(res, ROUND_DIGITS)

# v
def velocidad_triangular(y, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = ((gravity * y) / 2)**(1/2)
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_triangular(y, v, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = y + (v**2) / (2 * gravity)
    return round(res, ROUND_DIGITS)


## RECTANGULAR
# y
def tirante_critico_rectangular(Q, b, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = ((Q**2) / (gravity * b**2))**(1/3)
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_rectangular(b, y, SI):
    res = (b * y)
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_rectangular(b, SI):
    res = b
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_rectangular(b, y, SI):
    res = b + 2 * y
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_rectangular(b, y, SI):
    res = (b * y) / (b + 2 * y)
    return round(res, ROUND_DIGITS)

# v
def velocidad_rectangular(y, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = (gravity * y)**(1/2)
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_rectangular(y, v, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = y + (v**2) / (2 * gravity)
    return round(res, ROUND_DIGITS)


## TRAPEZOIDAL
# y
def tirante_critico_trapezoidal(Q, b, z, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    def fun_y(y):
        return gravity * z * y**2 + (gravity * b - 2 * z * Q**2) * y - b*Q**2 
    def dif_fun_y(y):
        return (2 * gravity * z * y) + gravity * b - 2 * z * Q**2

    y_o = 1000
    f_y = fun_y(y_o)
    dif_f_y = dif_fun_y(y_o)
    y_n = y_o - (f_y / dif_f_y)
    error = abs(y_o - y_n)
    y_o = y_n
    contador = 1
    print("yo = {}, y1 = {}, error = {}, iteracion = {}".format(y_o, y_n, error, contador))
    while error > ERROR:
        f_y = fun_y(y_n)
        dif_f_y = dif_fun_y(y_n)
        y_n = y_n - (f_y / dif_f_y)
        error = abs(y_o - y_n)
        y_o = y_n
        contador = contador + 1
        print("yo = {}, y{} = {}, error = {}, iteracion = {}".format(y_o, contador, y_n, error, contador))

    res = y_n
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_trapezoidal(b, y, z, SI):
    res = b * y + z * y**2
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_trapezoidal(b, y, z, SI):
    res = b + 2 * z * y
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_trapezoidal(b, y, z, SI):
    res = b + 2 * y * (1 + z**2)**(1/2)
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_trapezoidal(A, P, SI):
    res = A / P
    return round(res, ROUND_DIGITS)

# v
def velocidad_trapezoidal(Q, A, SI):
    res = Q / A
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_trapezoidal(y, v, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = y + (v**2) / (2 * gravity)
    return round(res, ROUND_DIGITS)


## CIRCULAR
# o / teta
def angulo_circular(D, Q, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    def fun_o(o):
        return (8 / D**2) * ((D * math.sin(o/2) * Q**2) / (gravity))**(1/3) + math.sin(o) - o

    def dif_fun_o(o):
        return (4 / 6 * D**2) * ((D * Q**2) / gravity)**(1/3)*(math.cos(o/2)/(math.sin(o/2))**(2/3)) + math.cos(o/2) - 1

    o_0 = math.pi
    f_o = fun_o(o_0)
    dif_f_o = dif_fun_o(o_0)
    o_n = o_0 - (f_o / dif_f_o)
    error = abs(o_0 - o_n)
    o_0 = o_n
    contador = 1
    print("o_0 = {}, o1 = {}, error = {}, iteracion = {}".format(o_0, o_n, error, contador))
    while error > ERROR:
        f_o = fun_o(o_0)
        dif_f_o = dif_fun_o(o_0)
        o_n = o_n - (f_o / dif_f_o)
        error = abs(o_0 - o_n)
        o_0 = o_n
        contador = contador + 1
        # print("o_0 = {}, o{} = {}, error = {}, iteracion = {}".format(o_0, contador, o_n, error, contador))

    res = o_n
    return round(res, ROUND_DIGITS)

# y
def tirante_critico_circular(o, D, SI):
    res = D/2 + (D/2) * math.cos(2*math.pi - o)
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_circular(o, D, SI):
    res = (o - math.sin(o)) * D / 8
    print(res)
    return round(res, ROUND_DIGITS)

# T
def espejo_de_agua_circular(o, D, SI):
    res = math.sin(o/2) * D
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_circular(o, D, SI):
    res = o * D / 2
    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_circular(o, D, SI):
    res = (1 - math.sin(o) / o) * D / 4
    return round(res, ROUND_DIGITS)

# v
def velocidad_circular(Q, A, SI):
    res = (Q / A)
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_circular(y, v, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG
    res = y + v**2 / ((v ** 2) / (2 * gravity))
    return round(res, ROUND_DIGITS)
