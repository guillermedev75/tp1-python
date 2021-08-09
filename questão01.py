#Aplicação para somar ímpares

#Função responsável por somar os termos ímpares
def somaTermos(termos):
    
    #Variavel
    soma = 0
    
    #Laço que soma os termos
    for termo in range(1, termos, 2):
        soma += termo
    
    #Onde é impresso o resultado da função
    print(f'\nA soma dos termos ímpares é {soma}')

#Receptor do dado do usuário
termos = int(input('Digite o número de termos: '))

#Onde a função é chamada
somaTermos(termos)