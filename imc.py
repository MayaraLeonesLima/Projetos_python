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
        if status ==