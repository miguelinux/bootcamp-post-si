#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Práctica 1: Fórmula General para Ecuaciones Cuadráticas
"""
import math

def main():
    a = float(input ('Introduzca a:'))
    b = float(input ('Introduzca b:'))
    c = float(input ('Introduzca c:'))

    if((b**2)-4*a*c) < 0:
        print("Solución con complejos")
    else:

    x1 = ( - b + math.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = ( - b - math.sqrt(b**2-(4*a*c)))/(2*a)
    
    print(x1)
    print(x2)
    

if __name__ == "__main__":
    main()

