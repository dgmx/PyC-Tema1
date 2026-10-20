# FinanzApp - Sesion 2: Operadores y expresiones (A.1.1)
# Objetivo: calcular porcentajes, redondear, convertir tipos y evitar errores.

IVA = 0.21          # 21 % de IVA (constante)
DESCUENTO = 0.10    # 10 % de descuento

print("=== Registro de un movimiento ===")

concepto = input("Concepto del movimiento: ")
importe_bruto = float(input("Importe bruto (EUR): "))

# aplica_descuento = input("¿Aplica descuento? (s/n): ").lower() == "s"

importe_iva = importe_bruto * IVA
importe_total = importe_bruto + importe_iva

print(f"Importe IVA: {importe_iva:.2f} EUR")
print(f"Importe total: {importe_total:.2f} EUR")
