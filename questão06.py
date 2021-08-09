#Aplicação para descobrir o tipo do triângulo

#Função para definir o tipo de triângulo
def tipoTriangulo(lados):
    
    #Variavel
    x, y, z = lados[0], lados[1], lados[2]
    
    #Verificação do tipo do triângulo
    if x < y + z and y < x + z and z < x + y:
        if x == y and y == z:
            retornoTringulo = '\nOs lados fornecidos são de um equilátero.'
        elif (x == y and x != z) or (x != y and x == z) or (x != z and y == z):
            retornoTringulo = '\nOs lados fornecidos são de um isósceles.'
        elif x != y and x != z and y != z:
            retornoTringulo = '\nOs lados fornecidos são de um escaleno.'
        return retornoTringulo, True
    
    #Erro nos dados do triângulo
    else:
        retornoTringulo = '\nOs lados fornecidos não se encaixam nas classificações de triângulos.'
        return retornoTringulo, False

#Entrada dos dados
x = int(input('Tamanho de X: '))
y = int(input('Tamanho de Y: '))
z = int(input('Tamanho de Z: '))

#Guardar os valores na tupla
lados = (x, y, z)

#Onde é impresso o resultado da aplicação
print(tipoTriangulo(lados)[0])