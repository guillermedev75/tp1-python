#Aplicação que calcula quantos dias você viveu

#Função que calcula o total de dias
def calcDias(idadeAnos, idadeMeses, idadeDias):

    #Variaveis de calculo
    idadeAnosDias = idadeAnos * 365
    totalDias = idadeAnosDias + idadeDias
    
    #Converter meses em dias
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    diasMes = 0
    for mes in range(idadeMeses):
        diasMes += meses[mes]
    
    #Soma do total de dias com a conversão dos meses em dias
    totalDias += diasMes
    
    #Onde é impresso o resultado da função
    print(f'Você viveu {totalDias} dias!')

#Entrada de dados
idadeAnos = int(input('Insira quantos anos você tem: '))
idadeMeses = int(input('Resto da sua idade em meses: '))
idadeDias = int(input('Resto da sua idade em dias: '))

#Onde a função é chamada
calcDias(idadeAnos, idadeMeses, idadeDias)