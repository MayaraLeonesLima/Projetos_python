#Ferramenta de Conversão Dolar x Real--
def converter(valor_dolar):
    taxa = 5.15
    valor_real = valor_dolar * taxa
    return valor_real
print("conversor Dólar x Real")
preco = float(input("Digite o Preço do Produto em Dólar: "))
resultado = converter(preco)
print(f"O valor em Reais é: {resultado:.2f}")