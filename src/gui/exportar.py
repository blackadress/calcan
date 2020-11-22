import math

GRAVITY = 9.80665
GRAVITY_ENG = 32.17404856
ERROR = 0.00001
ROUND_DIGITS = 5

Q = 2.5
D = 1.25

def angulo_circular(D, Q, SI):
    if SI:
        gravity = GRAVITY
    else:
        gravity = GRAVITY_ENG

    print(Q, gravity, D)

    C = (Q**2)*(8**3)/(gravity*D**5)
    def fun_y(o):
        return math.sin(o/2)*(1/2)*C - (o - math.sin(o))**3

    def dif_fun_y(o):
        return C*math.cos(o/2) - 3*((o-math.sin(o))**2)*(1-math.cos(o))

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

angulo_circular(D, Q, True)
