#etapa 1 - calculo imc
def calc_imc(imc):
    imc = peso/ (altura*altura)
    return imc

#etapa 2 - Classificação do imc
def classificacao_imc(resultado):
    if resultado >= 25:
        return "ACIMA DO PESO"
    else:
        return "PESO NORMAL"
    #etapa 3 - Mensagem de retorno
    def mensagem(status):
        if status == "ACIMA DO PESO":
            return "PROCURE UM MÉDICO!⚠️"
        else:
            return "peso ok"
#etapa 4 - integração do código
valor_peso = float(input("digite o seu peso"))
valor_altura = float(input("Digite a sua altura"))

valor_imc = calc_imc(valor_peso,valor_altura)
resultado_imc = classificar_imc(valor_imc)
saida = mensagem(resultado_imc)

print(f"n/")