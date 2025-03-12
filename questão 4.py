# limpar o terminal
import os 
os.system("clear || cls ")

quantidade_morango = float(input ("digite a quantidade de morangos: "))
quantidade_maca = float(input ("digite a quantidade de maças : "))
valor_total = float
valor_a_ser_pago = float

quantidade_frutas = quantidade_morango + quantidade_maca


if quantidade_frutas > 10 or valor_total > 15.00:
    desconto = valor_total * 0.10
    valor_a_ser_pago = valor_total - desconto

    print("\nExibindo os resultados .....")
    print (f"quantidade de morangos adquiridos em kg : {quantidade_morango}") 
    print (f"quantidade de maca adquiridos em kg : {quantidade_maca}") 
    print (f"valor total: {valor_total}") 
    print (f"valor do desconto : {desconto}") 
    print (f"valor a pagar : {valor_a_ser_pago}") 
    
else :
    print("\nExibindo os resultados .....")
    print (f"quantidade de morangos adquiridos em kg : {quantidade_morango}") 
    print (f"quantidade de maca adquiridos em kg : {quantidade_maca}") 
    print (f"valor a pagar : {valor_a_ser_pago}")