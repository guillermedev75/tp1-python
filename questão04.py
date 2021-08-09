#Aplicação para realizar calculos fatoriais

#Calculo fatorial do valor
def calculoFatorial(valorN):
    
    #Variaveis
    resultado = 1
    contador = 1

    #Laço que efetua o calculo
    while contador <= valorN:
        resultado *= contador
        contador += 1

    #Onde é impresso o resultado da função
    print(f'\nO fatorial de {valorN} é: {resultado}')

#Receptor do dado do usuário
valorN = int(input('Digite o valor de n: '))

#Verificação de números negativos
if valorN >= 0:
    calculoFatorial(valorN)
else:
    print('\nNão é possível calcular seu fatorial.')