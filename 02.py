numero =  int(input("Numero a ser buscado"))

valor1 = 0
valor2 = 1
 
while( True ):
    print((valor1 + valor2), end=' ')
    valor1 = valor2
    valor2 += valor1

    if( (valor1 + valor2) == numero):
        print('\nO numero', numero, 'existe na sequência.')
    elif ( (valor1 + valor2) > numero):
        print('\nO numero', numero, 'não está na sequência.')
        break