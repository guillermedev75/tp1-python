#Aplicação para alternar a posição das letras de um texto

# Função para alternar a posição das letras
def textoGirar(casasGirar, texto):

    #Variavel
    tamanho = len(texto)

    #algoritimo que alterna as casas
    if casasGirar == tamanho:
        resultado = texto[::-1]

        #Onde é impresso um resutlado da função
        print(f'\nResultado: {resultado}')
        
    else:
        if casasGirar > tamanho:
            casasGirar = casasGirar % tamanho

        inicio = texto[casasGirar:]
        final = texto[:casasGirar]
        resultado = inicio + final

        #Onde é impresso um resultado da função
        print(f'\nResultado: {resultado}')
 
#Entrada de dados
casasGirar = int(input('Posições a rotacionar para a esquerda: '))
texto = input('Insira o que deseja rotacionar: ')

#Onde a função é chamada
textoGirar(casasGirar, texto)