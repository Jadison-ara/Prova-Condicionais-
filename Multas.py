#Variáveis

limite = 80 #limite de velocidade em Km/h

multa_por_km = 20 # Valor da multa por Km excedido

#Entrada do usuario

velocidade = float (input ("Imforme a velocidade do carro em Km/h:"))

#Estrutura de condicão/calculo de verificação de velocidade

if velocidade > limite :
    excesso = velocidade - limite
    valor_multa = excesso * multa_por_km
    print (f"Vocé foi Multado! O Valor da Multa é R$ {valor_multa:.2f}")

else: 
    print("Velocidade dentro do limite.")


