# EXIGÊNCIA DE CÓDIGO 1 de 6: Mensagem de boas-vindas
print("Bem-vindos a minha loja! Eu me chamo Bruno Bezerra!")

# EXIGÊNCIA DE CÓDIGO 2 de 6: Input de um valor unitário e da quantidade de parcelas do produto
valor_pedido = float(input("Informe o valor do produto: "))
quantidadeparcelas = int(input("Informe a quantidade do parcelas: "))

# EXIGÊNCIA DE CÓDIGO 3 de 6: Implementação dos juros conforme a lista
if quantidadeparcelas< 4:
    juros= 0.00 #0%
elif 4 <= quantidadeparcelas< 6:
    juros = 0.04 #4%
elif 6 <= quantidadeparcelas<9:
    juros = 0.08 #8%
elif 9 <= quantidadeparcelas<13:
    juros = 0.16 #16%
else:
    juros= 0.32 #32%

# Cálculo do valor total com juros
valor_parcela= valor_pedido * (1+juros)/quantidadeparcelas
valor_total_parcelado= valor_parcela * quantidadeparcelas

# EXIGÊNCIA DE CÓDIGO 4 de 6: Exibir valores
print(f"Valor da parcela: R$ {valor_parcela:.2f}")
print(f"Valor total parcelado: R$ {valor_total_parcelado:.2f}")

# EXIGÊNCIA DE CÓDIGO 5 de 6: Estruturas if, elif e else já implementadas acima
# EXIGÊNCIA DE CÓDIGO 6 de 6: Comentários relevantes já inseridos no código
# EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2: Mensagem de boas-vindas já apresentada
# EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2: Valor da parcela e Valor total parcelado
