# limpar o terminal
import os 
os.system("clear || cls ")

valor_kg = input("""
tabela de frutas 
frutas \t até 5kg \t\t acima de 5kg
morangos \t R$ 2,50 por kg \t\t  R$ 2,20 por kg
maçã \t\t R$ 1,80 por kg \t R$ 1,50 por kg 
aperte ENTER para continuar : 
""")

kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))


preco_morango = 5.00 
preco_maca = 3.00 

valor_total = (kg_morango * preco_morango) + (kg_maca * preco_maca)


quantidade_total_kg = kg_morango + kg_maca
if quantidade_total_kg >= 10 or valor_total > 15:
    desconto = valor_total * 0.10  
    valor_final = valor_total - desconto
else:
    valor_final = valor_total

print(f"O valor a ser pago pelo cliente é: R$ {valor_final:.2f}")  
