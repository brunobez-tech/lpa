def criartabela(): #tabela que apresenta o menu
    print("Bem-vindos à marmitaria do Bruno Bezerra!") #EXIGÊNCIA DE CÓDIGO 1 DE 8
    print('\t CARDÁPIO')
    print ("-----------------------------------------------------------")
    print ('Bife Acebolado (BA):')
    print ('Tamanho P - 16 reais')
    print ('Tamanho M - 18 reais')
    print ('Tamanho G - 22 reais')
    print ('File de Frango (FF):')
    print ('Tamanho P - 15 reais')
    print ('Tamanho M - 17 reais')
    print ('Tamanho G - 21 reais')
    print ("-----------------------------------------------------------")
criartabela()
totalpedido = 0 #essa variável servirá como acumulador

while True: 
    sabor = input('\n Escolha o sabor (BA/FF):').strip().upper() #EXIGÊNCIA DE CÓDIGO 2 DE 8
    if sabor not in ['BA', 'FF']: #caso o cliente digite um sabor errado ele retorna ao inicio
        print('Sabor inválido, digite novamente')
        continue

    tamanho = input('Escolha o tamanho (P,M,G):').strip().upper() #EXIGÊNCIA DE CÓDIGO 3 DE 8
    if tamanho not in ['P', 'M', 'G']: #caso o cliente digite um tamanho errado ele retorna ao inicio
        print('Tamanho inválido, digite novamente')
        continue

    if sabor == 'BA': #EXIGÊNCIA DE CÓDIGO 4 DE 8
        if tamanho == 'P':
            preco = 16
        elif tamanho == 'M':
            preco = 18
        elif tamanho == 'G':
            preco = 22
    elif sabor == 'FF':
        if tamanho == 'P':
            preco = 15
        elif tamanho == 'M':
            preco = 17
        elif tamanho == 'G':
            preco = 21

    totalpedido += preco #EXIGÊNCIA DE CÓDIGO 5 DE 8, a variável totalpedido funciona como acumulador
    print(f'Pedido feito: {sabor} - {tamanho} - {preco} reais')
    maispedidos = input('Deseja realizar mais algum pedido? (sim/não):').strip().lower() #EXIGÊNCIA DE CÓDIGO 6 DE 8
    if maispedidos == 'sim': 
        continue #EXIGÊNCIA DE CÓDIGO 7 DE 8
    elif maispedidos =='nao' or maispedidos =='não':
        break
    else:
       print('Resposta inválida. Digite novamente!')
       continue

print(f'\n Total do pedido: {totalpedido} reais')