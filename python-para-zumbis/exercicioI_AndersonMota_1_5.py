def calcularDesconto():
    try:
        preco = input("Forneça o preço do produto:")
        desconto = input("Percentual de desconto:")
        valorDesconto = (preco / 100) * desconto
        preco = preco - valorDesconto
    except:
        print "Dados invalidos"
        calcularDesconto()
    else:
        print "Valor descontato: %.2f" %valorDesconto
        print "Preço com desconto: %.2f" %preco
    
calcularDesconto()