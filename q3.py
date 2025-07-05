def escolhamodelo(): #EXIGÊNCIA DE CÓDIGO 2 DE 7
    while True:
        modelo = input('Informe o modelo de camisa desejado(MCS/MLS/MCE/MLE):').upper() 
        if modelo == 'MCS':
            return 1.80
        elif modelo == 'MLS':
            return 2.10
        elif modelo == 'MCE':
            return 2.90
        elif modelo == 'MLE':
            return 3.20
        else: 
            print ('Opção inválida, digite novamente!')
#FUNÇÃO CRIADA PARA OBTER O NUMERO DE CAMISETAS E APLICA O VALOR DE DESCONTO

def numerocamisetas(): #EXIGÊNCIA DE CÓDIGO 3 DE 7
    while True:
        try:
            num = int (input('Informe o número de camisetas:')) 
            if num < 20:
                return num,0
            elif 20<= num < 200:
                return num,0.05
            elif 200<=num<2000:
                return num, 0.07
            elif 2000<=num<=20000:
                return num, 0.12
            else: 
                 print ('Numero de camisas inválido, digite novamente!')
        except ValueError:
            print ('Valor não numérico, digite novamente!')

def frete(): #EXIGÊNCIA DE CÓDIGO 4 DE 7
        while True:
            try: #EXIGÊNCIA DE CÓDIGO 6 DE 7
                print('\t FRETES DISPONÍVEIS')
                print ("-----------------------------------------------------------")
                tipofrete = int (input('\n \t 1 - Transportadora \n \t 2- Sedex \n \t 0- Retirada na fábrica):'))
                print ("-----------------------------------------------------------")
                if tipofrete == 1:
                    return 100
                elif tipofrete == 2:
                    return 200
                elif tipofrete == 0:
                    return 0
                else:
                    print ('Opção de frete inválida, digite novamente!')
            except ValueError:
                print ('Opção de frente inválida, digite novamente!') 

def main():
    print("Bem-vindos à fábrica de camisetas do Bruno Bezerra!") #EXIGÊNCIA DE CÓDIGO 1 DE 7
    print('\t CAMISETAS DISPONÍVEIS')
    print ("-----------------------------------------------------------")
    print ('Manga Curta Simples(MCS):')
    print ('Manga Longa Simples(MLS):') 
    print ('Manga Curta Estampada (MCE):')
    print ('Manga Longa Estampada(MLE):')
    print ("-----------------------------------------------------------")
    valormodelo = escolhamodelo()
    num, desconto = numerocamisetas()
    if num > 20000:
        print ('Valor de camisetas excede o permitido.')
        return
    valorfrete = frete()
    totalbruto = valormodelo * num 
    totaldesconto = totalbruto * desconto
    total = totalbruto - totaldesconto +valorfrete ##EXIGÊNCIA DE CÓDIGO 5 DE 7
    print (f"Modelo Escolhido:{'MCS' if valormodelo ==1.80 else 'MLS' if valormodelo ==2.10 else 'MCE' if valormodelo ==2.90 else 'MLE'}")
    print (f"Número de camisetas:{num}")
    print (f"Desconto aplicado:{desconto*100}%")
    print (f"Valor do frete: R$ {valorfrete:.2f}")
    print (f"Total a pagar:R$ {total:.2f}")
main()