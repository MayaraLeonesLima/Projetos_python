#Calculadora de Frete--Sistema de Logística--
def calcular_frete(peso):
    if peso <= 20:
        valor = peso * 10
    else:
        valor = peso * 15
    return valor

peso_carga = float(input("Digite o Peso da Carga em Kg: "))
frete = calcular_frete(peso_carga)
print(f"O Valor final do Frete é: R${frete:.2f}")

#Mayara Leones Lima 2F