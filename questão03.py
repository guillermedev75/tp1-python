#Aplicação para realizar um calculo fatorial

#Calculo fatorial do valor
def calculoFatorial(valorN):

    #Variavel
    resultado = 1
    
    #Laço que efetua o calculo
    for contador in range(1, valorN + 1):
        resultado *= contador

    #Onde é impresso o resultado da função
    print(f'\nO fatorial de {valorN} é: {resultado}')

#Entradas de dados
valorN = int(input('Digite o valor de n: '))

#Verificação do valor
if valorN >= 0:
    calculoFatorial(valorN)
else:
    print('\nNão é possível calcular seu fatorial.')