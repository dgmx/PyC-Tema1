# Sesión 3 — Estructuras de control condicionales (A.1.2)

# if / elif / else, condiciones anidadas, operador ternario.
# Práctica: clasificar un movimiento según signo (ingreso/gasto/cero) y avisar de saldo negativo.

# IVA = 0.21          # 21 % de IVA (constante)
# DESCUENTO = 0.10    # 10 % de descuento

print("=== Registro de un movimiento ===")

importe = float(input("Importe bruto (EUR): (positivo para ingreso, negativo para gasto): "))

if importe < 0:
    tipo = "gasto"
elif importe > 0:
    tipo = "ingreso"
else:
    tipo = "neutro"

signo = "+" if importe >= 0 else ""

print(f"Tipo de movimiento: {tipo}")
print(f"Importe: {signo}{importe} EUR")

saldo_actual = float(input("Ingrese su saldo actual (EUR): "))
saldo_resultante = saldo_actual + importe

if tipo == "gasto":
    if saldo_resultante < 0:
        print(f"¡Atención! Su saldo resultante es negativo. Saldo:{saldo_resultante} EUR")
    elif saldo_resultante == 0:
        print("¡Atención! Su saldo resultante es cero.")
    else:
        print("Su saldo resultante es positivo.")
else:
    print(f"Su saldo resultante es: {saldo_resultante} EUR")

          
