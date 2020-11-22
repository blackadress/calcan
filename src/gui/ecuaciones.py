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

## rectangular
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
        return (b*y + z*y**2)**3 - (b*Q**2)/gravity - (2*z*y*(Q**2))/gravity
    def dif_fun_y(y):
        return 3*((b*y + z*y**2)**2)*(b + 2*z*y) - (2*z*(Q**2))/gravity

    y_o = 100000
    # y_o = 0.3
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
    return round(abs(res), ROUND_DIGITS)

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

    C = (Q**2)*(8**3)/(gravity*D**5)
    def fun_y(o):
        return math.sin(o/2)*C - (o - math.sin(o))**3

    def dif_fun_y(o):
        return C*math.cos(o/2)*(1/2) - 3*((o-math.sin(o))**2)*(1-math.cos(o))

    y_o = 5
    contador = 1
    error = 50
    x = 0
    while error > ERROR:
        x = y_o - fun_y(y_o)/dif_fun_y(y_o)
        error = abs(x - y_o)
        print("yo = {}, y{} = {}, error = {}, iteracion = {}".format(y_o, contador, x, error, contador))
        y_o = x
        contador = contador + 1

    print("yo = {}, y{} = {}, error = {}, iteracion = {}".format(y_o, contador, x, error, contador))
    res = y_o
    return round(abs(res), ROUND_DIGITS)

# y
def tirante_critico_circular(o, D, SI):
    res = D/2 - (D/2) * math.cos(o/2)
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_circular(o, D, SI):
    res = (o - math.sin(o)) * D**2 / 8
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
    res = y + (v**2) / (2 * gravity)
    return round(res, ROUND_DIGITS)

## PARABOLA
# y
def tirante_critico_parabolico(Q, T, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG
    res = (3/2)*((Q**2)/(gravity*T**2))**(1/3)
    return round(res, ROUND_DIGITS)

# A
def area_hidraulica_parabolico(y, T, SI):
    res = (2/3)*T*y
    return round(res, ROUND_DIGITS)

# k
def foco_parabola(T, y, SI):
    res = (T**2)/(8*y)
    return round(res, ROUND_DIGITS)

# P
def perimetro_mojado_parabolico(T, y, A, SI):
    if y/T <= 0.25:
        print("menor 0.25")
        res = T + (8/3)*(y**2)/T
    elif abs(T - (3/2)*(A/y)) <= 0.1:
        t1 = (1 + (16*y**2)/T**2)**(1/2)
        print("t1", t1)
        t2 = 4*y/T + (1 + (16*y**2)/T**2)**(1/2)
        print("t2", t2)
        t3 = (T/(4*y))*(math.log(t2, math.e))
        print("t3", t3)
        res = (T/2)*(t1 + t3)
        print("res", res)
    else:
        res = 0

    return round(res, ROUND_DIGITS)

# R
def radio_hidraulico_parabolico(A, P, SI):
    res = A / P
    return round(res, ROUND_DIGITS)

# v
def velocidad_parabolico(Q, A, SI):
    res = Q / A
    return round(res, ROUND_DIGITS)

# E
def energia_especifica_parabolico(y, v, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    res = y + (v**2) / (2 * gravity)
    return round(res, ROUND_DIGITS)

