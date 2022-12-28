#!/usr/bin/python3

def check_cf(a, b, c):
    try:
        if complex(a) == 0:
            return False
        a = complex(a)
        b = complex(b)
        c = complex(c)
        return True
    except ValueError:
        return False

def check_complex_cf(a, b, c):
    if complex(a).imag != 0 or complex(b).imag != 0 or complex(c).imag != 0:
        return True
    else:
        return False

def discriminant(a, b, c):
    if check_complex_cf(a, b, c):
        return complex(b) ** 2 - (4*complex(a)*complex(c))
    else:
        return complex(b).real ** 2 - (4*complex(a).real*complex(c).real)

def root_x1(a, b, c):
    if check_complex_cf(a, b, c):
        return (-complex(b) + (discriminant(a, b, c))**0.5) / (2*complex(a))
    else:
        return (-complex(b).real + (discriminant(a, b, c))**0.5) / (2*complex(a).real)

def root_x2(a, b, c):
    if check_complex_cf(a, b, c):
        return (-complex(b) - (discriminant(a, b, c))**0.5) / (2*complex(a))
    else:
        return (-complex(b).real - (discriminant(a, b, c))**0.5) / (2*complex(a).real)
