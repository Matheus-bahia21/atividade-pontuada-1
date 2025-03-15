# limpar o terminal
import os 
os.system("clear || cls ")

Litro_gasolina = float(input("digite a quantidade de litros de gasolina: "))
Litro_alcool = float(input("digite a quantidade de litros de alcool_valor: "))

gasolina_valor = 6.59
alcool_valor = 3.79 
valor_pagar_gasolina = Litro_gasolina * gasolina_valor
valor_pagar_alcool = Litro_alcool * alcool_valor

if Litro_gasolina == 25: 
    valor_pagar_gasolina = (valor_pagar_gasolina * 2) / 100
    print(f"seu valor de desconto será: {valor_pagar_gasolina: 2f}")
elif Litro_gasolina > 25:
    valor_pagar_gasolina = (valor_pagar_gasolina * 4) / 100
    print (f"seu valor de desconto será: {valor_pagar_gasolina: 2f}")
else: 
    print("opção invalida")    

if Litro_alcool == 25: 
    valor_pagar_alcool = (valor_pagar_alcool * 3) / 100
    print(f"seu valor de desconto será: {valor_pagar_alcool: 2f}")
elif Litro_gasolina > 25:
    valor_pagar_alcool = (valor_pagar_alcool * 5) / 100
    print (f"seu valor de desconto será: {valor_pagar_alcool: 2f}")
else: 
    print("opção invalida")