def calcularDesconto():
    try:
        preco = float(input("Forneça o preço do produto:"))
        desconto = float(input("Percentual de desconto:"))
        valorDesconto = (preco / 100) * desconto
        preco = preco - valorDesconto
    except ValueError:
        print ("Dados informados são inválidos, devem conter apenas números.")
        calcularDesconto()
    else:
        print ("Valor descontato: %.2f" %valorDesconto)
        print ("Preço com desconto: %.2f" %preco)
    
calcularDesconto()