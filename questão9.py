# limpar o terminal
import os 
os.system("clear || cls ")

renda_mensal = float(input("digite sua renda mensal: "))
valor_total_emprestimo = renda_mensal* 10 
prestacao = (renda_mensal * 30 ) / 100
numero_parcelas = prestacao / valor_total_emprestimo


if renda_mensal >= 759:

 print("emprestimo concedido")   
else:
 print("emprestimo não concedido")   


 print(f"renda mensal {renda_mensal}")
 print(f"valor total do emprestimo {valor_total_emprestimo}")
 print(f"valor da parcela {prestacao}")
 print(f"numero de parcelas {numero_parcelas}") 