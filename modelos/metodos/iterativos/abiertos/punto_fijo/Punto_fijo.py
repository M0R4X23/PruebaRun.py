import  sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from .....extras.Funciones import errores, respuesta_json

class punto_fijo():

    def calcular_punto_fijo(json_data):
        x = sp.symbols("x")
        
        #obtener los valores del json
        f_x = sp.simplify(json_data["funcion"])
        g_x = sp.simplify(json_data["funcion_g_x"])
        g_prima = sp.diff(g_x)

        error_aceptado = float(json_data["tolerancia"])
        x_actual = float(json_data["xi"])
        x_anterior = 0

        iteracion = 0
        #Encabezados
        
        while True:
            iteracion += 1
            g_prima_evaluada = float(g_prima.subs(x, x_actual))
            g_x_evaluada = float(g_x.subs(x, x_actual))
            x_anterior = x_actual
            x_actual = g_x_evaluada
            error_acomulado = errores.error_aproximado_porcentual(x_anterior,x_actual)
            
            if(error_acomulado < error_aceptado):
                break
            elif g_prima_evaluada > 1:
                print("El metodo no converge")
                break
            
        print("La raiz aproximada es: ", x_actual)

