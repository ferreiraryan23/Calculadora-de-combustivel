km = float(input("Digite a quantidade de km rodado: "))
consumo = float(input("Digite o consumo do carro: "))
preco = float(input("Digite o preço do combustivel: "))
    
if km <= 0 or consumo <= 0 or preco <= 0:
    print("Os valores devem ser positivos")
else: 
    litros = km / consumo
    custo_total = preco * litros
    itros = round(litros, 2) 
    custo_total = round(custo_total, 2)
    
    print(f"A quantidade consumida durante a viagem foi: {litros}")
    print(f"O custo total da viagem foi de: {custo_total}")