# limpar o terminal
import os 
os.system("clear || cls ")

nome_do_produto = input("digite o nome do produto")
quantidade_adiquirida = float(input("digite a quantidade adquirida: "))
preco_unitario = float(input("digite o preço unitario do produto : "))

total = quantidade_adiquirida * preco_unitario

if quantidade_adiquirida <= 5:
    desconto = total * 0.80
    total_a_pagar = total - desconto
    print(f"total a pagar : {total_a_pagar}")
elif quantidade_adiquirida <= 5:
    desconto = total * 0
    total_a_pagar = total - desconto
    print(f"total a pagar : {total_a_pagar}")