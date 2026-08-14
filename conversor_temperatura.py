# Conversor de temperatura
# Converte Celsius para Fahrenheit e Fahrenheit para Celsius.

try:
    temperatura = float(input("Digite a temperatura: "))
    escala = input("Digite a escala (C para Celsius ou F para Fahrenheit): ").upper()

    if escala == "C":
        resultado = (temperatura * 9 / 5) + 32
        print(f"{temperatura:.1f}°C equivale a {resultado:.1f}°F")

    elif escala == "F":
        resultado = (temperatura - 32) * 5 / 9
        print(f"{temperatura:.1f}°F equivale a {resultado:.1f}°C")

    else:
        print("Escala inválida. Digite C ou F.")

except ValueError:
    print("Digite uma temperatura válida.")
